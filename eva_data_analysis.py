import matplotlib.pyplot as plt
import pandas as pd

# https://data.nasa.gov/resource/eva.json (with modifications)
data_in = open('./eva-data.json', 'r')
data_out = open('./eva-data.csv','w')
graph_file = 'myplot.png'


# read in json file
eva_data= pd.read_json(data_in,convert_dates['date'])
# convert eva colunm to float
eva_data['eva'] = eva_data['eva'].astype(float)
eva_data.dropna(axis=0, inplace=True)
eva_data.sort_values('date',inplace=True)


eva_data.to_csv(data_out, index=False)

eva_data['duration_hours'] = eva_data['duration'].str.split(":").apply(lambda x: int(x[0]) + int(x[1])/60)
eva_data['cumulative_time'] = eva_data['duration_hours'].cumsum()
plt.plot(eva_data['date'], eva_data['cumulative_time'], 'ko-')
plt.xlabel('Year')
plt.ylabel('Total time spent in space to date (hours)')
plt.tight_layout()
plt.savefig(graph_file)
plt.show()
