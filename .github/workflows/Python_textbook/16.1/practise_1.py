import csv
import matplotlib.pyplot as plt
import datetime
import numpy as np
from getDataClass import GetData

#Show mutiple columns in a single bar chart
#Compare rainfalls in Sikta & Death Vally at 2018

file_sk = 'Ch16\sitka_weather_2018_simple.csv'
file_dv = 'Ch16\death_valley_2018_simple.csv'
data_sk = GetData(file_sk)
data_dv = GetData(file_dv)                                                                                                                                                                          
rains = []

reader_sk = data_sk.readFile()
rains_sk = data_sk.getRains(reader_sk)
dates = data_sk.getDates(reader_sk)
reader_dv = data_dv.readFile()
rains_dv = data_dv.getRains(reader_dv)

width = 0.5
x = np.arange(len(dates))                                       

plt.style.use('seaborn' )
fig,ax = plt.subplots()
ax.bar(x, rains_sk, width, color='r',label='Sikta')
ax.bar(x + width, rains_dv, width, color='b',label='Death Valley')
ax.set_xticks(x)
ax.set_xticklabels(dates)
ax.legend()

ax.set_title('Precipitation Amount of Skita & Death Valley in 2018')
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('Rainfall', fontsize=16)
plt.show()