# prepare-CSVs-for-easyFRAPweb

## Installation
Clone the repository and create the conda environment with the provided environment.yml file using the instructions [here]( https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file).


## Usage
1. Open Anaconda Prompt
2. Activate the conda environment called pandas
```
conda activate pandas
```
3. Navigate to where your directory is. You may need to change from the `C:` drive to the `D:` drive first which can be done by entering:
```
D:
```
before using `cd` to change directories. For example:
```
cd D:\Will\2022-07-12_prepare-FRAP-csv
```
4. Run the Python script with your directory paths and parameters.

```
(pandas) D:\Will>python prepareCSVforeasyFRAP.py -h
usage: prepareCSVforeasyFRAP.py [-h] [--inputDir INPUTDIR] [--outputDir OUTPUTDIR] [--bleachFrameNumber BLEACHFRAMENUMBER] [--frameInterval FRAMEINTERVAL]

options:
  -h, --help            show this help message and exit
  --inputDir INPUTDIR   Input directory of CSVs from ImageJ/FIJI to be processed (default: None)
  --outputDir OUTPUTDIR
                        Output directory of processed CSVs for easyFRAPweb (default: None)
  --bleachFrameNumber BLEACHFRAMENUMBER
                        Frame number corresponding to the bleaching, starting from 0 (default: 3)
  --frameInterval FRAMEINTERVAL
                        Time between timepoints (assumed to be seconds) (default: 10)
```

Example:

`(pandas) D:\Will\2022-07-12_prepare-FRAP-csv>python prepareCSVforeasyFRAP.py --inputDir .\02-CSVs_from_Fiji\WT\ --outputDir .\03-CSVs_processed_for_easyFRAPweb\WT\`
