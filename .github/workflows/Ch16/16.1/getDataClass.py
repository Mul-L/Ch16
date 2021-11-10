import csv 
import datetime

class GetData:
    def __init__(self, file):
        self.file = file
    
    def readFile(self):
        list = []
        with open(self.file) as f:
            reader = csv.reader(f)
            header = next(f)           
            for row in reader:
                list.append(row)
        return list

    def getRains(self, reader): 
        rains = []      
        for row in reader:
            try:
                rain = float(row[3])
            except ValueError:
                print(f"Error happened at {row[2]}")
            else:
                rains.append(rain)
        return rains

    def getDates(self, reader):  
        dates = []     
        for row in reader:
            try:
                date = datetime.datetime.strptime(row[2], '%Y-%m-%d') 
            except ValueError:
                print(f"Error happened at {date}")
            else:
                dates.append(date)
        return dates
    
    def getTemperature(self, reader):
        highs = []
        for row in reader:
            try:
                high = int(row[4]) 
            except ValueError:
                print(f'Error happened at {row[2]}')
            else:
                highs.append(high)
        return highs