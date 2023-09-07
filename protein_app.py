import numpy as np
import pandas as pd
import streamlit as st

from protein_distribution import RESULTS_DIR
from protein_distribution.protein_info import get_protein_categories, get_proteins
from protein_distribution.uniprot import (
    UniprotMetadata,
    read_metadata,
    read_uniprot_mapping,
)
from protein_distribution.visualization import (
    plot_protein_abundance,
    plot_protein_histogram,
)


st.set_page_config(
    page_title=None,
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items=None,
)
padding_top = 0

st.markdown(
    """
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 1rem;
                }
        </style>
        """,
    unsafe_allow_html=True,
)

uniprot2sid = read_uniprot_mapping()
sid2uniprot = {v: k for k, v in uniprot2sid.items()}


@st.cache_data
def load_data():
    # Load data
    df_abundance = pd.read_excel(RESULTS_DIR / "data.xlsx", sheet_name="Abundance")
    del df_abundance["comments"]
    df_abundance["sid"] = df_abundance["study"] + "_" + df_abundance["source"]
    proteins = get_proteins(df_abundance, uniprot=True)
    protein_categories = get_protein_categories(proteins)
    mddict = read_metadata()

    return df_abundance, proteins, protein_categories, mddict


# Create a text element and let the reader know the data is loading.
# data_load_state = st.text('Loading data...')
# Load data.
df_abundance, proteins, protein_categories, mddict = load_data()
# Notify the reader that the data was successfully loaded.
# data_load_state.text('Loading data...done!')

st.sidebar.title("Protein distribution")

st.sidebar.header("Protein")
selected_species = st.sidebar.multiselect(
    label="Select species",
    options=["Homo sapiens"],
    default=["Homo sapiens"],
)
selected_protein_categories = st.sidebar.multiselect(
    "Select protein classes",
    options=["cyp", "ugt", "abc", "slc", "other"],
    default=["cyp", "ugt", "abc", "slc"],
)

proteins = []
for category in selected_protein_categories:
    proteins += protein_categories[category]

protein_id = st.sidebar.selectbox("Select protein", proteins)

# st.sidebar.header('Filter options')
# selected_tissues = st.sidebar.multiselect(
#     label='Select tissues',
#     options=["liver microsomes", "hepatocyte", "jejunum"],
#     default=["liver microsomes", "hepatocyte"],
# )


uniprot_id = sid2uniprot[protein_id]
md: UniprotMetadata = mddict.entries[uniprot_id]

# main window content
st.title(f"{protein_id} - {md.protein}")
st.markdown(
    f"""[**{md.id}** ({md.name})](https://www.uniprot.org/uniprotkb/{md.id}/entry)
Genes: `{md.gene}`
Organism: `{md.organism}`
"""
)

col1, col2 = st.columns(2)
with col1:
    fig = plot_protein_abundance(
        data=df_abundance, protein_id=protein_id, image_dir=None
    )
    st.pyplot(fig)

with col2:
    fig = plot_protein_histogram(
        data=df_abundance, protein_id=protein_id, image_dir=None
    )
    st.pyplot(fig)

df_protein = df_abundance[df_abundance.protein == protein_id]
st.dataframe(df_protein, use_container_width=True)
