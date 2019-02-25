from flask import Flask, jsonify, request, render_template, session, redirect
import time
app = Flask(__name__)
@app.route('/add', methods=['POST'])
def add_value():
    with open("sounddatatest.txt", "a+") as textfile:
        values = request.get_json()
        required = ['value']
        if not all(k in values for k in required):
            return 'Missing values', 400
        for line in values['value']:
            textfile.write("{}\t{} \r\n".format(line[0], line[1]))
        print(values['value'])
        print(values['value'][0][0])
        return 'Done!'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=80)
