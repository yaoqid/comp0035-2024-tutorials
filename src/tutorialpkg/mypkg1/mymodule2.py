from pathlib import Path
import pandas as pd


def describe_dataframe(df: pd.DataFrame):
    """
    This function accepts a pandas DataFrame and prints out
    basic information describing the data.    
    Parameters:
    df (pd.DataFrame): The DataFrame containing the data.   
    Returns:
    None
    """
    print("DataFrame Info:")
    print(df.info())
    print("\nDataFrame Description:")
    print(df.describe())


def main():
    try:
        # Filepath for the CSV file using Path with __file__
        csv_file = Path(__file__).parent.parent.joinpath('data', 'paralympics_events_raw.csv')      
        # Check if CSV file exists
        if csv_file.exists():
            # Reading CSV data into a DataFrame
            paralympics_csv_df = pd.read_csv(csv_file)
            print("CSV file read successfully.\n")
            describe_dataframe(paralympics_csv_df)
        else:
            print(f"The file {csv_file} does not exist.")       
        # Filepath for the Excel file using Path with __file__
        excel_file = Path(__file__).parent.parent.joinpath('data', 'paralympics_all_raw.xlsx')
        # Check if Excel file exists
        if excel_file.exists():
            # Reading the first worksheet of the Excel file
            paralympics_excel_df = pd.read_excel(excel_file, sheet_name=0)
            print("\nFirst worksheet of Excel file read successfully.\n")
            describe_dataframe(paralympics_excel_df)           
            # Reading the second worksheet ('medal_standings')
            paralympics_medals_df = pd.read_excel(excel_file, sheet_name='medal_standings')
            print("\nSecond worksheet ('medal_standings') read successfully.\n")
            describe_dataframe(paralympics_medals_df)
        else:
            print(f"The file {excel_file} does not exist.")
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
    except UnicodeDecodeError as e:
        print(f"UnicodeDecodeError: {e}")
    except ImportError as e:
        print(f"ImportError: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
