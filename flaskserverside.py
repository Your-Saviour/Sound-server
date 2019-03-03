#!/usr/bin/python3
from flask import Flask, jsonify, request, render_template, session, redirect
import time
import random
import glob
app = Flask(__name__)
curent_sound = {1: 0, 2: 0}
locations = {1: "basment", 2: "kictchen"}
ipdict = {1:'', 2:''}
@app.route('/')
def page1():
    return render_template("page1.html")

@app.route('/update')
def noot():
    global curent_sound
    global locations
    return "At {} it is {}. <br> At {} it is {}".format(locations[1], curent_sound[1], locations[2], curent_sound[2])

@app.route('/admin')
def controls():
    listoffiles = list(glob.glob('static/*.txt'))
    return render_template("guiint.html", listoffiles=listoffiles)

@app.route('/change', methods=['POST'])
def changer():
    if "Location_1" in request.form:
        locations[1] = request.form.get("Location_1")
    if "Location_2" in request.form:
        locations[2] = request.form.get("Location_2")
    return redirect('/admin')

@app.route('/ipaddr')
def ips():
    global ipdict
    return str(ipdict)


@app.route('/add', methods=['POST'])
def add_value():
    global curent_sound
    global locations
    global ipdict
    values = request.get_json()
    required = ['time', 'db','sensornum', 'ip dict']
    if not all(k in values for k in required):
        return 'Missing values', 400
    sensornum = values["sensornum"]
    location = locations[sensornum]
    if sensornum == 1:
        ipdict[1] = values['ip dict']
    if sensornum == 2:
        ipdict[2] = values['ip dict']
    with open("static/{}.txt".format(location), "a+") as textfile:
        textfile.write("{}\t{}\t \r\n".format(values['db'], values['time'], values['sensornum']))
        curent_sound[sensornum] = values['db']
        return 'Done!'


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=80)
