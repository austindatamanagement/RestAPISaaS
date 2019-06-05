import os
import cx_Oracle
from flask import Flask
import json

app = Flask(__name__)

username = "Your username"
password = "Your password"
service_name = "Your service name"

connection_detail = username+"/"+password+"@"+service_name

@app.route('/channels')
def channels():
    connection = cx_Oracle.connect(connection_detail)
    cur = connection.cursor()
    cur.execute("select * from channels")
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