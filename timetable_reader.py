import csv
from datetime import time, datetime, date
from pprint import pprint

LESSON_START_TIME = {
     'T' : time(8,40),
     '1' : time(8,50),
     '2' : time(9,40),
     '3' : time(11,00),
     '4' : time(11,50),
     '5' : time(12,40),
     '6' : time(13,50),
     '7' : time(14,40)
}



lessons = []

with open('timetableData.csv') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
          lessons.append(row)
          #print(row['Day'], row['Lesson'], row['Subject'], row['Room'], 'starts at', LESSON_START_TIME[row['Lesson']])

#pprint(lessons)

def filter_lessons_by_day(lessons, day):   
     output_list = []
     for lesson in lessons:
          if lesson['Day'] == day:
               output_list.append(lesson)
     
     return output_list

     
def get_period_from_time(t):
     if t < time(8,50):
          return 'T'
     elif t < time(9,40):
          return '1'
     elif t < time(11,00):
          return '2'
     elif t < time(11,50):
          return '3'
     elif t < time(12,40):
          return '4'
     elif t < time(13,50):
          return '5'
     elif t < time(14,40):
          return '6'
     elif t < time(15,30):
          return '7'

#print(get_period_from_time(time(9,00))) #should be '1'
#print(get_period_from_time(time(15,00))) #should be '7'

#def get_first_lesson_after_time(lessons, time)

def filter_lessons_by_period(lessons, period):
     period_list = []
     for lesson in lessons:
          if lesson['Lesson'] == period:
               period_list.append(lesson)
     
     return period_list 


def filter_lessons_by_C4SL(lessons):
     period_list = []
     for lesson in lessons:
          print(lesson)
          if lesson['Room'].startswith('LS'):
               period_list.append(lesson)
     return period_list 
     
def get_lessons_from_datetime(d):
     t = d.time()
     weekday = str(d.isoweekday())
     period = get_period_from_time(t)
     
     c4sl_lessons = filter_lessons_by_C4SL(lessons)
     
     days_lessons = filter_lessons_by_day(c4sl_lessons, weekday) #should return lessons for that day
     return filter_lessons_by_period(days_lessons, period)

pprint(get_lessons_from_datetime(datetime.now()))