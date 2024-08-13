import csv

def delete_rows_in_csv(filename,start,end):
    with open(filename,'r') as file:
        reader = csv.reader(file)
        rows = [row for i, row in enumerate(reader) if i < start or i > end]

    with open(filename,'w',newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

delete_rows_in_csv('CCD2_20231230 .csv',752506,802299)
