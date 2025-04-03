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


w=csv.writer(data_out)



time = []
date =[]

j=0
for i in eva_data:
    print(eva_data[j])
    # and this bit
    w.writerow(eva_data[j].values())
    if 'duration' in eva_data[j].keys():
        tt=eva_data[j]['duration']
        if tt == '':
            pass
        else:
            t=dt.datetime.strptime(tt,'%H:%M')
            ttt = dt.timedelta(hours=t.hour, minutes=t.minute, seconds=t.second).total_seconds()/(60*60)
            print(t,ttt)
            time.append(ttt)
            if 'date' in eva_data[j].keys():
                date.append(dt.datetime.strptime(eva_data[j]['date'][0:10], '%Y-%m-%d'))
                #date.append(data[j]['date'][0:10])

            else:
                time.pop(0)
    j+=1

t=[0]
for i in time:
    t.append(t[-1]+i)

date,time = zip(*sorted(zip(date, time)))



plt.plot(date,t[1:], 'ko-')
plt.xlabel('Year')
plt.ylabel('Total time spent in space to date (hours)')
plt.tight_layout()
plt.savefig(g_file)
plt.show()
