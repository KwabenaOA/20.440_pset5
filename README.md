# The Effect of Protein Subcellular Localization on MHC Class I Antigen Presentation
This repository contains the code and data necessary to reproduce figures for visualizing endogenous HLA class I-associated peptides. The work completed in the repository will eventually become part of a larger project, so the main directory and subdirectories were structured with that in mind. 

All data supplied in this repository was originally collected and supplemented from the paper *A large peptidome dataset improves HLA class I epitope prediction across most of the human population.* Sarkizova et al. 2020.
## Reproducing analyses
The following guidelines will illustrate how you can reproduced the 95 visualization figures corresponding to all 95 single-allele HLA-A, -B, -C, and -G mono-allelic cell lines. Each figure will display the total intensity of the HLA class I-associated peptides associated with the given allele.
### Installation Requirements and Execution
To reproduced all of the figures, you'll first need to install the required modules.

You should use a Python 3 virtual environment. Below is a series of commands that you can use to create an empty conda environment, install pip, and then pip install the relavant packages to run the code.

In a command prompt window, type the following which in the main directory:

```
conda create -n pset5_git python=3
source activate pset5_git
conda install pip
pip install -r requirements.txt
```

After executing the previous lines, the virtual environment should be set up and all relevant packages should be installed.

To produce the 95 visualization figures, you will need to navigate to the ```src``` directory and run the ```MHC_data_plot.py``` program. This is done by executing the following commands:

```
cd src
python MHC_data_plot.py
```

The figures will appear in a newly-created directory: ```/figures/MHC_visualization```. The total runtime for all the figures should be on the order of 5 minutes depending on your computer's configuration.
### Directory Structure
**Data**
All data is located in the folder ```raw_data/```:
- ```MHC_data/```: Contains data related to endogenous HLA class I-associated peptides. Each file under this directory is a semicolon-sepearted document (ssv) containing elution column chromatography data used to examine binding affinity between a set of HLA peptides and MHC class I proteins—more information can be found in the original paper by Sarkizova et al.

**Source Code**
All finalized code is located in the folder ```src/```:
- ```MHC_data_plot.py```: Python code that takes in data related to endogenous HLA class I-associated peptides and outputs figures visualizing the data. The purpose of this code is to determine that all files and data under ```raw_data/MHC_data/``` are accessible.

**Jupyter Notebook Code**
All non-finalized code is located in the folder ```jupyter_notebooks/```:
- ```MHC_data_plot.ipynb```: IPython notebook containing code similar to ```MHC_data_plot.py```. I would suggest tinkering with this code file if you are attempting to alter and/or debug ```MHC_data_plot.py```.

**Figures**
All figures will appear under the folder ```figures/```:
- ```original_MHC_visualization/```: Contains all the plots that visualize the peptide data that's populated under each of the 95 HLA cell lines (found in ```raw_data/MHC_data/```). These are the original plots which can be reproduced by following the **Installation Requirements and Execution** guidelines above.
- ```MHC_visualization/```: Contains all the reproduced plots that visualize the peptide data that's populated under each of the 95 HLA cell lines (found in ```raw_data/MHC_data/```). ```MHC_visualization``` will only be created after ```MHC_data_plot.py``` is run.
