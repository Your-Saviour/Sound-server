import math
import time
from datetime import datetime
import requests
from netifaces import interfaces, ifaddresses, AF_INET

def calculate_rms(sound_levels):
    squared = []
    for i in sound_levels:
        squared.append(i**2)

    new = sum(squared)
    e = math.sqrt(new)
    return(e)

def scale(x1, y1, x2, y2, x):
    numerator = y2*(x1 - x) + y1*(x - x2)
    denominator = x1 - x2

    number = numerator/denominator

    return number


import subprocess

import serial
ser = serial.Serial('/dev/cu.wchusbserial1410', 115200)  # open serial port
print(ser.name)         # check which port was really used

i = 0

sound_levels = []

while True:

    value_as_string = ser.readline().decode('utf-8').strip()
    value_as_int = int(value_as_string)

    i = i + 1

    sound_levels.append(value_as_int)


    if i == 100:
        rms = calculate_rms(sound_levels) #* 0.275
        log_rms = math.log(rms)
        print(log_rms)

        decibels = scale(3.6, 40, 5.6, 80, log_rms)
        #print(datetime.now(), decibels, ' db')


        date = datetime.now()
        bigdict = {}
        for ifaceName in interfaces():
            addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
            addressesnew = ', '.join(addresses)
            if addressesnew != 'No IP addr':
                bigdict[ifaceName] = addressesnew
        data_to_send = {'time' : date.isoformat(), 'db' : decibels, 'sensornum': 1, 'ip dict': bigdict}
        #print(data_to_send)
        resp = requests.post('http://localhost:10001/add', json=data_to_send)
        #print(resp.text)
        i = 0
        sound_levels = []

ser.close()
