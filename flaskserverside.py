from flask import Flask, jsonify, request, render_template, session, redirect
import time
import random
app = Flask(__name__)
curent_sound = 0
@app.route('/')
def page1():
    return render_template("page1.html")

@app.route('/update')
def noot():
    global curent_sound
    return str(curent_sound)

@app.route('/add', methods=['POST'])
def add_value():
    global curent_sound
    with open("sounddatatest.txt", "a+") as textfile:
        values = request.get_json()
        required = ['value']
        if not all(k in values for k in required):
            return 'Missing values', 400
        for line in values['value']:
            textfile.write("{}\t{} \r\n".format(line[0], line[1]))
            curent_sound = line[0]
        print(values['value'])
        print(values['value'][0][0])
        return 'Done!'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=80)
