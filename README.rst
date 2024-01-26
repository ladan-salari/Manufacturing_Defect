======================
Manufacturing Defect
======================

:Author: Ladan Salari Sharif
:Maintainer: Ladan Salari Sharif
:Language: Python 3.7
:Project: Manufacturing Imperfections in Hollow Mictolattices



Installation
++++++++++++
**Windows:**

**Mac:**

Developement
++++++++++++
pip install -e .

Contributing
++++++++++++
1. Clone the repository and use `requirementstxt` to set up your virtual environment.

2. Set up the pre-commit hook:

.. code-block:: bash

    pre-commit install




Installing
++++++++++++
**Use the following line to pip install this code**

pip install git+https://github.com/ladan-salari/Manufacturing_Defect.git


Files
++++++++++++
**create_input_files_nanoct.py**

    Create input files for different load cases on beams extracted from nano-ct imaging.

**create_input_files_cylinder_geometry.py**

    Create geometries of perfect cylindrical beams based on average beam length and diameter in nano-ct data.
**create_input_files_cylinder.py**

    Create simulation input files for perfect cylindrical beams based on average beam length and diameter in nano-ct data.

**create_input_file_imperfect_beams.py**

    Create 2000 imperfect beams using stochastic models based on nano-ct data.

**eigen_value_extraction_nanoct.py**

    Post-process simulation results for different load cases on beams extracted from nano-ct imaging.

**eigen_value_extraction_cylinder.py**

    Post-process simulation results for perfect cylindrical beams based on average beam length and diameter in nano-ct data.

**eigen_value_extraction_Imperfect_beams.py**

    Post-process the 2000 imperfect beams created using stochastic models based on nano-ct data.



