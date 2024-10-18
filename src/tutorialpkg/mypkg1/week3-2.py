import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def plot_timeseries(df, group_by_type=True):
    """
    Function to plot timeseries data showing the number of participants over time.
    
    Parameters:
    df (pd.DataFrame): The DataFrame containing the event data.
    group_by_type (bool): If True, groups the data by the 'type' column before plotting.
    
    Returns:
    None
    """
    if group_by_type:
        # Group by 'type' and plot for each group separately
        grouped = df.groupby('type')
        for group_name, group_df in grouped:
            plt.figure(figsize=(10, 5))
            plt.title(f"Participants Over Time - {group_name.capitalize()} Events")
            group_df.plot(x='start', y='participants', ax=plt.gca(), marker='o', linestyle='-', label='Total Participants')
            plt.ylabel('Number of Participants')
            plt.xlabel('Year')
            plt.grid(True)
            plt.savefig(f'participants_over_time_{group_name}.png')  # Save the plot as an image
            plt.show()
    else:
        # Plot without grouping
        df.plot(x='start', y='participants', figsize=(10, 5), marker='o', linestyle='-', label='Total Participants')
        plt.ylabel('Number of Participants')
        plt.xlabel('Year')
        plt.grid(True)
        plt.show()

def plot_male_female_timeseries(df):
    """
    Function to plot timeseries data for male and female participants over time.
    
    Parameters:
    df (pd.DataFrame): The DataFrame containing the event data.
    
    Returns:
    None
    """
    plt.figure(figsize=(10, 5))
    plt.title("Male and Female Participants Over Time")
    
    # Plot male participants
    df.plot(x='start', y='participants_m', ax=plt.gca(), marker='o', linestyle='-', label='Male Participants')
    
    # Plot female participants
    df.plot(x='start', y='participants_f', ax=plt.gca(), marker='o', linestyle='-', label='Female Participants', color='orange')
    
    plt.ylabel('Number of Participants')
    plt.xlabel('Year')
    plt.grid(True)
    plt.legend()
    plt.savefig('male_female_participants_over_time.png')  # Save the plot as an image
    plt.show()

if __name__ == "__main__":
    # Path to the prepared CSV file
    prepared_data_csv = Path(__file__).parent.parent.joinpath("data", "paralympics_events_prepared.csv")

    # Read the prepared data into a DataFrame
    try:
        df_prepared = pd.read_csv(prepared_data_csv, parse_dates=['start'])
    except FileNotFoundError as e:
        print(f"File not found. Please check the file path. Error: {e}")
        df_prepared = None

    if df_prepared is not None:
        # Create the timeseries plot for participants grouped by event type
        print(df_prepared)
        plot_timeseries(df_prepared)

        # Challenge: Plot male and female participants over time
        #plot_male_female_timeseries(df_prepared)
