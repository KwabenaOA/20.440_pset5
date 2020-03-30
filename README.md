# The Effect of Protein Subcellular Localization on MHC Class I Antigen Presentation
This repository contains the code and data to reproduce figures for visualizing endogenous HLA class I-associated peptides.

All data supplied in this repository was originally collected and supplemented from the paper *A large peptidome dataset improves HLA class I epitope prediction across most of the human population.* Sarkizova et al. 2020.
## Reproducing analyses
The following guidelines will how to reproduced the 95 visualization figures corresponding to all 95 single-allele HLA-A, -B, -C, and -G mono-allelic cell lines. Each figure will display the total intensity of the HLA class I-associated peptides associated with the given allele.
### Installation Requirements
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

To produce the 95 visualization figures, you will need to navigate to the **src** directory and run the **MHC_data_plot.py** program. This is done by executing the following commands:

```
cd src
python MHC_data_plot.py
```

The figures will appear in a newly-created directory: **./figures/MHC_visualization**. The total runtime for all the figures should be on the order of 5 minutes varying on your computer's configuration.
### Directory Structure
