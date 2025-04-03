import matplotlib.pyplot as plt
import pandas as pd
'''
Script to read, clean and plot NASA EVA data.
This uses data from https://data.nasa.gov/resource/eva.json (with modifications)
The script will plot and save a figure of cumulative time in space.
'''

print(f'Reading input file {data_in}')
# Opening input and output files and setting graph file name
data_in = open('./eva-data.json', 'r')
data_out = open('./eva-data.csv','w')
graph_file = 'myplot.png'

print('Cleaning data')
# read in the data as a pandas dataframe
eva_data= pd.read_json(data_in,convert_dates['date'])
# convert eva colunm to float
eva_data['eva'] = eva_data['eva'].astype(float)
# get rid of missing values
eva_data.dropna(axis=0, inplace=True)
# sort by date
eva_data.sort_values('date',inplace=True)

# write sorted and cleaned data to csv
eva_data.to_csv(data_out, index=False)

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
