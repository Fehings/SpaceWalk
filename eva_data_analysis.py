import datetime as dt
import json
import csv
import matplotlib.pyplot as plt

# https://data.nasa.gov/resource/eva.json (with modifications)
data_in = open('./eva-data.json', 'r')
data_out = open('./eva-data.csv','w')
g_file = 'myplot.png'

fieldnames = ("EVA #", "Country", "Crew    ", "Vehicle", "Date", "Duration", "Purpose")

eva_data=[]


for i in range(374):
    line=data_in.readline()
    print(line)
    eva_data.append(json.loads(line[1:-1]))
#data.pop(0)
## Comment out this bit if you don't want the spreadsheet


writeout=csv.writer(data_out)



time = []
date =[]

j=0
for i in eva_data:
    print(eva_data[j])
    # and this bit
    writeout.writerow(eva_data[j].values())
    if 'duration' in eva_data[j].keys():
        duration=eva_data[j]['duration']
        if duration == '':
            pass
        else:
            eva_dur=dt.datetime.strptime(duration,'%H:%M')
            eva_dur_sec = dt.timedelta(hours=eva_dur.hour, minutes=eva_dur.minute, seconds=eva_dur.second).total_seconds()/(60*60)
            print(eva_dur,eva_dur_sec)
            time.append(eva_dur_sec)
            if 'date' in eva_data[j].keys():
                date.append(dt.datetime.strptime(eva_data[j]['date'][0:10], '%Y-%m-%d'))
                #date.append(data[j]['date'][0:10])

            else:
                time.pop(0)
    j+=1

eva_dur=[0]
for i in time:
    eva_dur.append(eva_dur[-1]+i)

date,time = zip(*sorted(zip(date, time)))



plt.plot(date,eva_dur[1:], 'ko-')
plt.xlabel('Year')
plt.ylabel('Total time spent in space to date (hours)')
plt.tight_layout()
plt.savefig(g_file)
plt.show()
