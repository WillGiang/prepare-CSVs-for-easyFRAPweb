import pandas as pd
import sys
import os
import argparse

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--inputDir", help="Input directory of CSVs from ImageJ/FIJI to be processed")
parser.add_argument("--outputDir", help="Output directory of processed CSVs for easyFRAPweb")
parser.add_argument("--bleachFrameNumber", help="Frame number corresponding to the bleaching, starting from 0", default=3)
parser.add_argument("--frameInterval", help="Time between timepoints (assumed to be seconds)", default=10)

if len(sys.argv)==1:
    parser.print_help(sys.stderr)
    sys.exit(1)

args = parser.parse_args()

def prepareCSVforeasyFRAP(CSV, bleach_frame_number = 3, FRAME_INTERVAL = 10):
    """
    Process a CSV file for easyFRAPweb.

    Generate the column for time and merge with a dataframe
    with only the mean intensity measurements of three ROIs.

    Parameters
    ----------
    CSV : str
        Full path to a CSV file created from ImageJ/FIJI
    bleach_frame_number : int, default 3
        Timepoint corresponds to the bleaching frame, starting from 0
    FRAME_INTERVAL : int, default 10
        Time interval during imaging experiment

    Returns
    -------
    DataFrame
        easyFRAPweb-ready DataFrame to be saved 
    """
    df = pd.read_csv(CSV)
    
    # Fiji includes a column with a nearly blank header " "
    # which we will rename to "Timepoint"
    df.rename({' ' : 'Timepoint'},
        axis = 'columns',
        inplace = True
        )
    
    # Convert timepoints to seconds with the initial timepoint at 0
    df["Time[sec]"] = (df["Timepoint"] - 1) * FRAME_INTERVAL

    ## Only keep columns that have Mean because easyFRAPweb can't handle more than four columns
    df_mean = df.loc[:, df.columns.str.contains("Mean")]
    

    df_merged = pd.merge(
        df["Time[sec]"],
        df_mean,
        left_index  = True,
        right_index = True,
        )
    
    # Drop the bleach frame row because it isn't useful
    df_merged = df_merged.drop(index = bleach_frame_number)    

    return df_merged


def main():
    input_CSV_dir  = args.inputDir
    output_CSV_dir = args.outputDir

    output_CSV_dir_exists = os.path.exists(output_CSV_dir)

    if not output_CSV_dir_exists:
        os.makedirs(output_CSV_dir)

    input_CSVs = os.listdir(input_CSV_dir)

    for f in input_CSVs:
        f_path = os.path.join(input_CSV_dir, f)

        df = prepareCSVforeasyFRAP(f_path, args.bleachFrameNumber, args.frameInterval)

        ## Save results to output CSV directory
        df.to_csv(
            os.path.join(output_CSV_dir, f),
            index=False
            )

if __name__ == "__main__":
    main()