import csv
from datetime import time
from pprint import pprint

LESSON_START_TIME = {
     'T' : time(8,40),
     '1' : time(8,50),
     '2' : time(9,40),
     '3' : time(11,00),
     '4' : time(11,50),
     '5' : time(12,40),
     '6' : time(1,50),
     '7' : time(2,40)
}

lessons = []

with open('timetableexport.csv') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
          lessons.append(row)
          #print(row['Day'], row['Lesson'], row['Subject'], row['Room'], 'starts at', LESSON_START_TIME[row['Lesson']])

#pprint(lessons)

def get_all_lessons_for_day(lessons, day):   
     some_list = []
     for lesson in lessons:
          if lesson['Day'] == day:
               some_list.append(lesson)
     
     return some_list

#def get_lesson_number_from_time(t):
 #    for TIME in LESSON_START_TIME:
  #        if TIME{T} < 
   #  return TIME



for TIME in LESSON_START_TIME:
     if TIME{T} < time(8,50):
          print('k')

#print(get_lesson_number_from_time(time(9,00))) #should be '1'
#print(get_lesson_number_from_time(time(3,00))) #should be '7'

#def get_first_lesson_after_time(lessons, time)


wed_lessons = get_all_lessons_for_day(lessons, '3') #should return Wednesday's lessons
pprint(wed_lessons)

