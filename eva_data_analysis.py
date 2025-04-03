import matplotlib.pyplot as plt
import pandas as pd
'''
Script to read, clean and plot NASA EVA data.
This uses data from https://data.nasa.gov/resource/eva.json (with modifications)
The script will plot and save a figure of cumulative time in space.
'''

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
    duration_hours = int(hours) + int(minutes)/6
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





# Opening input and output files and setting graph file name
graph_file = 'myplot.png'
input_file = open('./eva-data.json', 'r', encoding="utf-8")
eva_data=read_json_to_dataframe(input_file)

write_dataframe_to_csv(eva_data,'./eva-data.csv')

plot_cumulative_time(eva_data,graph_file)





