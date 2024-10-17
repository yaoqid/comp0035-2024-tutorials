import pandas as pd
from pathlib import Path

def prepare_data(events_df: pd.DataFrame, npc_codes_df: pd.DataFrame):
    """
    Function to merge two dataframes: 'events' and 'npc_codes' based on country names
    and drop unnecessary columns.
    
    Parameters:
    events_df (pd.DataFrame): The DataFrame containing event data with 'country' column.
    npc_codes_df (pd.DataFrame): The DataFrame containing NPC codes with 'Name' and 'Code' columns.

    Returns:
    pd.DataFrame: The prepared DataFrame with columns removed and merged.
    """
    # Drop unnecessary columns
    df_prepared = events_df.drop(columns=['URL', 'disabilities_included', 'highlights'], axis=1)
    
    # Merge the dataframes using 'left' join based on 'country' and 'Name'
    df_prepared = df_prepared.merge(npc_codes_df, how='left', left_on='country', right_on='Name')
    
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
        
        # Print the remaining column names after dropping the unnecessary ones
        print("Remaining columns after dropping 'URL', 'disabilities_included', and 'highlights':")
        print(df_prepared.columns)
    
    except FileNotFoundError as e:
        print(f"File not found. Please check the file path. Error: {e}")
