import csv
with open('timetableexport.csv') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
          print(row[''], row[''])