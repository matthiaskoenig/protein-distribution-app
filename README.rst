.. image:: https://github.com/matthiaskoenig/protein-distribution-app/raw/main/docs/images/favicon/protein-distribution-app-100x100-300dpi.png
   :align: left
   :alt: protein-distribution-app logo

protein-distribution-app: database of protein variability of CYP, UGT, ABC and SLC in human liver
=================================================================================================

.. image:: https://img.shields.io/pypi/v/protein-distribution.svg
   :target: https://pypi.org/project/protein-distribution/
   :alt: Current PyPI Version

.. image:: https://img.shields.io/pypi/pyversions/protein-distribution.svg
   :target: https://pypi.org/project/protein-distribution/
   :alt: Supported Python Versions

.. image:: https://img.shields.io/pypi/l/protein-distribution.svg
   :target: http://opensource.org/licenses/LGPL-3.0
   :alt: GNU Lesser General Public License 3

.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.8331377.svg
   :target: https://doi.org/10.5281/zenodo.8331377
   :alt: Zenodo DOI

The objective of this project is to provide a systematic overview of protein variability of CYP450, UGT, ABC and SLC isoforms in the human liver. Relationships within protein isoforms (e.g., subgroups such as sex or ethnicity) and between CYP450 isoforms (e.g., correlations) will be studied. The project will provide an important resource to elucidate factors affecting individual drug metabolism and for computational modeling of drug detoxification by the liver.

Streamlit protein distribution app.

How to cite
===========

.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.8331377.svg
   :target: https://doi.org/10.5281/zenodo.8331377
   :alt: Zenodo DOI

Installation
============
To run the example applications install the requirements::

    cd protein-distribution-app
    mkvirtualenv protein_app --python=python3.12
    (protein_app) pip install -r requirements.txt

Run app
=======
To run the app use::

    streamlit run protein_app.py

License
=======

* Source Code: `LGPLv3 <http://opensource.org/licenses/LGPL-3.0>`__
* Documentation: `CC BY-SA 4.0 <http://creativecommons.org/licenses/by-sa/4.0/>`__

The protein-distribution-app source is released under both the GPL and LGPL licenses version 2 or
later. You may choose which license you choose to use the software under.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License or the GNU Lesser General Public
License as published by the Free Software Foundation, either version 2 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU General Public License for more details.

Funding
=======
Matthias König is supported by the Federal Ministry of Education and Research (BMBF, Germany)
within the research network Systems Medicine of the Liver (**LiSyM**, grant number 031L0054)
and by the German Research Foundation (DFG) within the Research Unit Programme FOR 5151
`QuaLiPerF <https://qualiperf.de>`__ (Quantifying Liver Perfusion-Function Relationship in Complex Resection - A Systems Medicine Approach) by grant number 436883643 and by grant number
465194077 (Priority Programme SPP 2311, Subproject SimLivA).

© 2022-2024 Matthias König
