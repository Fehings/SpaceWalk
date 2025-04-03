import matplotlib.pyplot as plt
import pandas as pd
'''
Script to read, clean and plot NASA EVA data.
This uses data from https://data.nasa.gov/resource/eva.json (with modifications)
The script will plot and save a figure of cumulative time in space.
'''

def read_json_to_dataframe(input_file):
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
    df.to_csv(outfile, index=False)



# Opening input and output files and setting graph file name
input_file = open('./eva-data.json', 'r', encoding="utf-8")
eva_data=read_json_to_dataframe(input_file)

write_dataframe_to_csv(eva_data,'./eva-data.csv')

graph_file = 'myplot.png'


print('Plotting cumulative space walk data')
# plot the cumulative time spent in space and save the figure
eva_data['duration_hours'] = eva_data['duration'].str.split(":").apply(lambda x: int(x[0]) + int(x[1])/60)
eva_data['cumulative_time'] = eva_data['duration_hours'].cumsum()
plt.plot(eva_data['date'], eva_data['cumulative_time'], 'ko-')
plt.xlabel('Year')
plt.ylabel('Total time spent in space to date (hours)')
plt.tight_layout()
plt.savefig(graph_file)
plt.show()
