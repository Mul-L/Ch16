import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'Ch16\death_valley_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            high = int(row[4])    
            date = datetime.strptime(row[2], '%Y-%m-%d')
            low = int(row[5])
        except ValueError:
            print(f"Missing date for {date}")
        else:
            highs.append(high)
            dates.append(date)       
            lows.append(low)
    
    plt.style.use('seaborn')   
    fig,ax = plt.subplots()
    ax.plot(dates, highs, c='red', alpha=0.5)
    ax.plot(dates, lows,c='blue', alpha=0.5)
    ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    ax.set_title("Daliy highest temperature in 2018")
    ax.set_xlabel('', fontsize=16)
    ax.set_ylabel('temperature(F)', fontsize=16)

    plt.show()