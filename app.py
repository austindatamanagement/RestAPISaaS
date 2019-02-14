import os
import cx_Oracle
from flask import Flask
import json

app = Flask(__name__)

@app.route('/benchmark')
def benchmark():
    connection = cx_Oracle.connect("admin/DemoATP12345678@demoatp_high")
    cur = connection.cursor()
    cur.execute("select * from benchmark")
    list = []
    for result in cur:
        list.append(result)
        print (result)
    list_json = json.dumps(list)
    cur.close()
    connection.close()
    return list_json

@app.route('/vesseltakedown')
def vesseltakedown():
    connection = cx_Oracle.connect("admin/DemoATP12345678@demoatp_high")
    cur = connection.cursor()
    cur.execute("select * from vesseltakedown")
    list = []
    for result in cur:
        list.append(result)
        print (result)
    list_json = json.dumps(list)
    cur.close()
    connection.close()
    return list_json

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5000)