import csv

#Get the index by knowned column name

def getIndex(file):
    dates_index = ''
    highs_index = ''
    rainfall_index = ''

    with open(file) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for index, column in enumerate(header_row):
            if column == "DATE":
                dates_index = index
            if column == "TMAX":
                highs_index = index
            if column == "PRCP":
                rainfall_index = index

    return dates_index, highs_index, rainfall_index
