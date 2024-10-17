

# from tutorialpkg.mypkg2.mymodule2_1 import calculate_area_of_circle
# from tutorialpkg.mypkg2.mymodule2_2 import fetch_user_data
from pathlib import Path
import pandas as pd

'''mock_database = {
    1: {'name': 'Alice', 'email': 'alice@example.com', 'age': 30},
    42: {'name': 'Bob', 'email': 'bob@example.com', 'age': 45},
}'''


def describe_dataframe(df: pd.DataFrame):
    """
    This function accepts a pandas DataFrame and prints out 
    detailed information describing the data, including:
    - Shape
    - First and last 5 rows
    - Column labels
    - Column datatypes
    - Info summary
    - Statistical description of numerical data    
    Parameters:
    df (pd.DataFrame): The DataFrame containing the data.   
    Returns:
    None
    """
    # Print the shape of the DataFrame (number of rows and columns)
    print("Shape of the DataFrame:", df.shape)  
    # Print the first and last 5 rows of the DataFrame
    print("\nFirst 5 rows of the DataFrame:")
    print(df.head())   
    print("\nLast 5 rows of the DataFrame:")
    print(df.tail())   
    # Print all columns (ensure all columns are visible)
    pd.set_option("display.max_columns", None)   
    # Print column labels
    print("\nColumn labels:", df.columns.tolist())   
    # Print the column data types
    print("\nColumn data types:")
    print(df.dtypes)   
    # Print the info of the DataFrame
    print("\nDataFrame Info:")
    print(df.info())   
    # Print statistical description of the DataFrame
    print("\nStatistical Summary:")
    print(df.describe())


def prepare_data(df: pd.DataFrame, columns_to_change: list):
    """
    Function to prepare the data by converting certain columns to integer types and fixing date columns.
    """
    # Convert specified float64 columns to int64
    for column in columns_to_change:
        if df[column].isnull().any():
            print(f"Column '{column}' contains NaN values. Filling NaN with 0 before conversion.")
            df[column] = df[column].fillna(0)
        df[column] = df[column].astype('int64')
    
    # Convert 'start' and 'end' columns to datetime
    print("\nUnique values in 'start' column:")
    print(df['start'].unique())
    
    print("\nUnique values in 'end' column:")
    print(df['end'].unique())
    
    # Convert to datetime format (assumes the format is day/month/year)
    df['start'] = pd.to_datetime(df['start'], format='%d/%m/%Y', errors='coerce')
    df['end'] = pd.to_datetime(df['end'], format='%d/%m/%Y', errors='coerce')
    
    # Check for any remaining invalid datetime conversions
    if df['start'].isnull().any() or df['end'].isnull().any():
        print("Warning: There are invalid date entries after conversion.")
    
    return df


'''def prepare_data(df: pd.DataFrame, columns_to_change: list):
    """
    Function to convert specified float64 columns to int64, handling NaN values first.
    
    Parameters:
    df (pd.DataFrame): The DataFrame containing the data.
    columns_to_change (list): List of column names to convert from float64 to int64.

    Returns:
    pd.DataFrame: The modified DataFrame with specified columns converted to int.
    """
    for column in columns_to_change:
        if df[column].isnull().any():
            print(f"Column '{column}' contains NaN values. Filling NaN with 0 before conversion.")
            # Fill NaN values with 0 or another placeholder
            df[column] = df[column].fillna(0)
        
        # Convert the column to integer type
        df[column] = df[column].astype('int64')
    
    return df'''


if __name__ == "__main__":
    try:
        # Filepath of the csv data file
        paralympics_datafile_csv = Path(__file__).parent.parent.joinpath("data", "paralympics_events_raw.csv")
        events_csv_df = pd.read_csv(paralympics_datafile_csv)
        
        # Columns that you want to convert from float to int
        columns_to_change = ['countries', 'events', 'participants_m', 'participants_f', 'participants']
        
        # Prepare the data by changing float64 to int64
        events_csv_df = prepare_data(events_csv_df, columns_to_change)
        
        # Call the function to describe the dataframe
        describe_dataframe(events_csv_df)
    
    except FileNotFoundError as e:
        print(f"File not found. Please check the file path. Error: {e}")


'''if __name__ == '__main__':
    # The functions are in the modules in mypkg2. You will need to import them.

    # Calculate the area of a circle with a radius of 10. Print the result.
    area = calculate_area_of_circle(10)
    print(f"The area is {area}.")

    # Use the fetch_user_data(user_id, database) function to print the data
    # for the user with ID 42 that is in `mock_database` variable.
    print(fetch_user_data(42, mock_database))

    # Locate the data file `paralmpics_raw.csv` relative to this file using
    # pathlib.Path. Prove it exists.

csv_file = Path(__file__).parent.parent.joinpath('data', 'paralympics_events_raw.csv')
if csv_file.exists():
    print(f"CSV file found: {csv_file}")
else:
    print("CSV file not found.")'''