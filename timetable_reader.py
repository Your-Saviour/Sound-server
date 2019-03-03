import csv
from datetime import time

LESSON_START_TIME = {
     'T' : time(8,40),
     '1' : time(8,50),
     '2' : time(9,40),
     '3' : time(11,00),
     '4' : time(11,50),
     '5' : time(12,30),
     '6' : time(1,50),
     '7' : time(2,40)
     
}

with open('timetableexport.csv') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
          print(row['Day'], row['Lesson'], row['Subject'], row['Room'], 'starts at', LESSON_START_TIME[row['Lesson']])