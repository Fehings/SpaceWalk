import matplotlib.pyplot as plt
import pandas as pd
import sys
import re

'''
Script to read, clean and plot NASA EVA data.
This uses data from https://data.nasa.gov/resource/eva.json (with modifications)
The script will plot and save a figure of cumulative time in space.
'''

def main(input_file, output_file, graph_file):
    eva_data = read_json_to_dataframe(input_file)
    eva_data = add_crew_size_column(eva_data)
    write_dataframe_to_csv(eva_data,output_file)
    plot_cumulative_time(eva_data,graph_file)
    print("EVA analysis has finished")


def calculate_crew_size(crew):
    """
    Calculate the size of the crew for a single crew entry

    Args:
        crew (str): The text entry in the crew column containing a list of crew member names

    Returns:
        (int): The crew size
    """
    if crew.split() == []:
        return None
    else:
        return len(re.split(r';', crew))-1

def add_crew_size_column(df):
    """
    Add crew_size column to the dataset containing the value of the crew size

    Args:
        df (pd.DataFrame): The input data frame.

    Returns:
        df_copy (pd.DataFrame): A copy of df with the new crew_size variable added
    """
    print('Adding crew size variable (crew_size) to dataset')
    df_copy = df.copy()
    df_copy["crew_size"] = df_copy["crew"].apply(
        calculate_crew_size
    )
    return df_copy

def read_json_to_dataframe(input_file):
    '''
    Read the data from a JSON file into pandas dataframe
    Clean the data by removing incomplete rows and sort by date
    
    Args:
        input_file(str): The path to the JSON file
        
    Returns:
        eva_df (pd.DataFrame): The cleaned and sorted data as a dataframe
        '''
    # read in the data as a pandas dataframe
    eva_data= pd.read_json(input_file, convert_dates=['date'])
    # convert eva colunm to float
    print('Cleaning data')
    eva_data['eva'] = eva_data['eva'].astype(float)
    # get rid of missing values
    eva_data.dropna(axis=0, inplace=True)
    # sort by date
    eva_data.sort_values('date',inplace=True)
    return eva_data


def write_dataframe_to_csv(df, outfile):
    '''
    Write a pandas dataframe to a csv file
    
    Args:
        df (pd.DataFrame): the pandas dataframe you want to write
        outfile (str): The file name you want to write to

    Returns:
        No returns to python, but it should create a csv file for you in the location you specify!

    '''
    df.to_csv(outfile, index=False)


def text_to_duration(duration):
    hours, minutes = duration.split(":")
    duration_hours = int(hours) + int(minutes)/60
    return duration_hours


def add_duration_hours(df):
    """
    Add a new column 'duration_hours' to the DataFrame 'df' by applying the 'text_to_duration' function to the 'duration' column.
    Parameters:
    - df (pandas.DataFrame): The input DataFrame.
    Returns:
    - pandas.DataFrame: A new DataFrame with the 'duration_hours' column added.
    """
    df_copy = df.copy()
    df_copy['duration_hours'] = df_copy['duration'].apply(
        text_to_duration
        )
    return df_copy


def plot_cumulative_time(df, graph_file):
    """
    Plot the cumulative time spent in space over the years.
    Parameters:
    - df (pandas.DataFrame): The input DataFrame containing space walk data.
    - graph_file (str): The file path to save the generated graph.
    Returns:
    None
    """
    df = add_duration_hours(df)
    df['cumulative_time'] = df['duration_hours'].cumsum()

    print('Plotting cumulative space walk data')
    plt.plot(df['date'], df['cumulative_time'], 'ko-')
    plt.xlabel('Year')
    plt.ylabel('Total time spent in space to date (hours)')
    plt.tight_layout()
    plt.savefig(graph_file)
    plt.show()




if __name__ == "__main__":
    if len(sys.argv) < 3:
        input_file = './data/eva-data.json'
        output_file = './results/eva-data.csv'
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]

    # Opening input and output files and setting graph file name
    graph_file = './results/cumulative_eva_graph.png'
    main(input_file, output_file, graph_file)







