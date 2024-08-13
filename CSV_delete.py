import csv

with open('CCD2_20231228 .csv' , 'r') as file:
    reader = csv.reader(file)

    rows = [row for row in reader if any(row)]

with open('CCD2_20231228 .csv','w',newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)
    print('CCD2_20231228 .csv')