import argparse
import pandas as pd


def read_file(input_file_path):
    """
    Helper method to read a given file into a dataframe
    :param input_file_path: Path to input file
    :return: Dataframe
    """
    try:
        df = pd.read_csv(input_file_path)
        return df
    except FileNotFoundError:
        raise Exception("Input file '{}' does not exist".format(input_file_path))
    except Exception:
        raise Exception("Something went wrong while reading the input file.")


def merge_dataframes(df1, df2, merge_column):
    """
    Helper method to merge two dataframes on a common merge column
    :param df1: First Dataframe
    :param df2: Second Dataframe
    :param merge_column: Common column to merge the two dataframes on
    :return: Merged Dataframe
    """
    try:
        merged_df = pd.merge(df1, df2, on=merge_column)
        return merged_df
    except KeyError:
        raise Exception("Error: The specified join column {} does not exist in one of the datasets.".format(merge_column))
    except Exception:
        raise Exception("Something went wrong while merging the input files.")


def save_as_csv(output_file_path, df):
    """
    Helper method to save a given dataframe as csv file
    :param output_file_path: Path to output file to be saved as CSV
    :param df: Output dataframe to be saved as CSV
    """
    df.to_csv(output_file_path, index=False)
    print("New output file '{}' generated".format(output_file_path))


if __name__ == "__main__":
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description='Merge CSV files')

    # Add arguments
    parser.add_argument('--file1', type=str, help='Path to input file 1')
    parser.add_argument('--file2', type=str, help='Path to input file 2')
    parser.add_argument('--output_path', type=str, help='Path to output file')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Access the values of the arguments
    path1 = args.file1
    path2 = args.file2
    output_path = args.output_path
    try:
        df1 = read_file(path1)
        df2 = read_file(path2)
        merged_df = merge_dataframes(df1, df2, "CompanyID")
        save_as_csv(output_path, merged_df)
        print("Number of companies: {}".format(merged_df["CompanyID"].count()))
    except Exception as ex:
        print(ex)