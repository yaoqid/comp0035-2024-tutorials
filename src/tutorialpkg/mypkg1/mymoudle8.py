import pandas as pd
from pathlib import Path

def prepare_data(events_df: pd.DataFrame, npc_codes_df: pd.DataFrame):
    """
    Function to clean and merge two dataframes: 'events' and 'npc_codes' based on country names,
    handle missing values, drop unnecessary columns, and clean the 'type' column.
    
    Parameters:
    events_df (pd.DataFrame): The DataFrame containing event data with 'country' column.
    npc_codes_df (pd.DataFrame): The DataFrame containing NPC codes with 'Name' and 'Code' columns.

    Returns:
    pd.DataFrame: The prepared DataFrame with missing values handled and unnecessary columns removed.
    """
    # Replace country names using the provided dictionary
    replacement_names = {
        'UK': 'Great Britain',
        'USA': 'United States of America',
        'Korea': 'Republic of Korea',
        'Russia': 'Russian Federation',
        'China': "People's Republic of China"
    }
    events_df['country'] = events_df['country'].replace(replacement_names)
    
    # Drop unnecessary columns
    df_prepared = events_df.drop(columns=['URL', 'disabilities_included', 'highlights'], axis=1)
    
    # Remove rows with missing participant data (Rome 1960) and future events (indices 0, 17, 31)
    df_prepared = df_prepared.drop(index=[0, 17, 31])
    
    # Reset the index after dropping rows
    df_prepared = df_prepared.reset_index(drop=True)
    
    # Clean the 'type' column: strip whitespaces and convert to lowercase
    df_prepared['type'] = df_prepared['type'].str.strip().str.lower()
    
    # Merge the dataframes using 'left' join based on 'country' and 'Name'
    df_prepared = df_prepared.merge(npc_codes_df, how='left', left_on='country', right_on='Name')
    
    # Drop the 'Name' column after merging
    df_prepared = df_prepared.drop(columns=['Name'], axis=1)
    
    return df_prepared

if __name__ == "__main__":
    try:
        # Filepath of the npc_codes.csv data file
        npc_codes_csv = Path(__file__).parent.parent.joinpath("data", "npc_codes.csv")
        paralympics_datafile_csv = Path(__file__).parent.parent.joinpath("data", "paralympics_events_raw.csv")
        
        # Read the events data
        events_df = pd.read_csv(paralympics_datafile_csv)

        # Read the npc_codes.csv with only 'Code' and 'Name' columns
        npc_codes_df = pd.read_csv(npc_codes_csv, encoding='utf-8', encoding_errors='ignore', usecols=['Code', 'Name'])
        
        # Print unique values for 'type' column before cleaning
        print("Unique values in 'type' column before cleaning:")
        print(events_df['type'].unique())

        # Prepare the data
        df_prepared = prepare_data(events_df, npc_codes_df)
        
        # Print the remaining column names after preparation
        print("\nRemaining columns after preparation:")
        print(df_prepared.columns)
        
        # Print unique values for 'type' column after cleaning
        print("\nUnique values in 'type' column after cleaning:")
        print(df_prepared['type'].unique())
    
    except FileNotFoundError as e:
        print(f"File not found. Please check the file path. Error: {e}")
