import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def plot_histograms(df, columns=None):
    """
    Function to plot histograms for the specified columns in the DataFrame.
    
    Parameters:
    df (pd.DataFrame): The DataFrame containing the data.
    columns (list): List of columns to create histograms for. If None, plots all numeric columns.
    
    Returns:
    None
    """
    if columns:
        # Plot histograms for the specified columns
        df[columns].hist(bins=10, figsize=(10, 5))
    else:
        # Plot histograms for all numeric columns
        df.hist(bins=10, figsize=(10, 5))
    
    # Show the plot
    plt.show()

if __name__ == "__main__":
    # Path to the prepared CSV file
    prepared_data_csv = Path(__file__).parent.parent.joinpath("data", "paralympics_events_prepared.csv")

    # Read the prepared data into a DataFrame
    try:
        df_prepared = pd.read_csv(prepared_data_csv)
    except FileNotFoundError as e:
        print(f"File not found. Please check the file path. Error: {e}")
        df_prepared = None
    
    if df_prepared is not None:
        # Create histograms for 'participants_m' and 'participants_f'
        plot_histograms(df_prepared, columns=['participants_m', 'participants_f'])

        # Challenge: Create histograms for summer and winter events separately
        summer_df = df_prepared[df_prepared['type'] == 'summer']
        winter_df = df_prepared[df_prepared['type'] == 'winter']
        
        print("\nGenerating histograms for Summer events...")
        plot_histograms(summer_df, columns=['participants_m', 'participants_f'])
        
        print("\nGenerating histograms for Winter events...")
        plot_histograms(winter_df, columns=['participants_m', 'participants_f'])
