import os
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

"""
Description: Obtains the raw MHC ssv files and presents them as pandas dataframes.
             Each dataframe is sorted by 'score' (a metric to rank each peptide's MHC binding association).
Returns: A list of pandas dataframe objects, each representing a ssv file.
"""
def get_raw_data():
    # Current Working Directory: ./20.440-term-project/jupyter_notebooks
    data_path = os.path.realpath('..')
    for child_dir in ['raw_data','MHC_data']:
        data_path = os.path.join(data_path, child_dir)
    
    dataframes = []
    for file in os.listdir(data_path):
        if file[-3:] != 'ssv':
            continue
        ssv_path = os.path.join(data_path,file)
        dataframes.append((pd.read_csv(ssv_path, sep=';'),file[:5]))
    
    return dataframes

"""
Description: Produces a figure showing the total intensity of each peptide
             and the relative rankings of each peptide.
Params:
    - dataframe: pandas dataframe containing raw MHC ssv file data
    - tag: elution information
    - file_name: name under which the file will be saved
    - sort: field by which the data will be sorted on the x-axis
            (in ascending order)
Returns: Figure showing peptide intensities.
"""
def peptide_lineplot(dataframe, tag, file_name, sort='totalIntensity'):
    fig, ax = plt.subplots(figsize=(5, 5))
    df = dataframe.sort_values(sort)[['totalIntensity', 'sequence']]
    df['log(totalIntensity)'] = np.log(df['totalIntensity'])
    df['rank'] = range(len(dataframe))
    
    sns.lineplot(x='rank', y='log(totalIntensity)', data=df)
    ax.set_title('Peptide Binding Intensities for HLA-'
                 + tag[0] + ' (' + tag[1:3] + ':' + tag[3:] + ')',
                 size='13')
    ax.set(ylabel='Total Intensity (log_10)', xlabel='Peptide Rank')
    sns.set(style='whitegrid')
    
    plt.tight_layout()
    figure_path = os.path.realpath('..')
    for new_dir in ['figures','MHC_visualization']:
        figure_path = os.path.join(figure_path,new_dir)
        if not os.path.exists(figure_path):
            os.mkdir(figure_path)
    
    fig.savefig(os.path.join(figure_path,file_name), dpi=300)
    plt.close()

if __name__ == "__main__":
    allele_dataframes = get_raw_data()
    for i in range(len(allele_dataframes)):
        frame, tag = allele_dataframes[i]
        peptide_lineplot(frame, tag, 'Peptide Binding Intensities (' + tag + ').png')
