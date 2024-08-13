import csv

with open('CCD0_20231222 .csv','r') as f:
    reader = csv.reader(f)
    rows = [list(map(str.strip, row)) for row in reader]
    print(rows)