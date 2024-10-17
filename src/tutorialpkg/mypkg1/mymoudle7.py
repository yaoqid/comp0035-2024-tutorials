import pandas as pd
from pathlib import Path

def prepare_data(events_df: pd.DataFrame, npc_codes_df: pd.DataFrame):
    """
    Function to clean and merge two dataframes: 'events' and 'npc_codes' based on country names,
    handle missing values, and drop unnecessary columns.
    
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
    
    # Drop the 'Name' column after merging
    df_prepared = events_df.drop(columns=['URL', 'disabilities_included', 'highlights'], axis=1)
    
    # Remove rows with missing participant data (Rome 1960) and future events (indices 17, 31)
    df_prepared = df_prepared.drop(index=[0, 17, 31])
    
    # Reset the index after dropping rows
    df_prepared = df_prepared.reset_index(drop=True)
    
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
        
        # Prepare the data
        df_prepared = prepare_data(events_df, npc_codes_df)
        
        # Print the remaining column names and check for missing values
        print("Remaining columns after preparation:")
        print(df_prepared.columns)
        
        # Print rows with any missing values
        missing_rows = df_prepared[df_prepared.isna().any(axis=1)]
        if missing_rows.empty:
            print("No missing values in the dataset.")
        else:
            print("Rows with missing values:")
            print(missing_rows)
    
    except FileNotFoundError as e:
        print(f"File not found. Please check the file path. Error: {e}")
