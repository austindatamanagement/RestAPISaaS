import os
import cx_Oracle
from flask import Flask
import json
import numpy as np

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

@app.route('/video')
def video():
    connection = cx_Oracle.connect("admin/DemoATP12345678@demoatp_high")
    cur = connection.cursor()
    cur.execute("""
    declare
    begin
    dbms_cloud.put_object( 
    'OBJ_STORE_CRED', 
    'https://swiftobjectstorage.us-phoenix-1.oraclecloud.com/v1/gse00014475/VideoBucket/Neurological_Surgery_.mp4'
    );
    end;
    """)

@app.route('/average')
def average():
    connection = cx_Oracle.connect("admin/DemoATP12345678@demoatp_high")
    cur = connection.cursor()
    cur.execute("select * from benchmark")
    list_benchmark = []
    bleeding = []
    efficiency =[]
    complexity = []
    for result in cur:
        print (type(result))
        list_benchmark.append(result)
        bleeding.append(result[1])
        efficiency.append(result[2])
        complexity.append(result[3])
        print (result)
    avg_bleeding = sum(bleeding)/ float(len(bleeding))
    avg_efficiency = sum(efficiency)/ float(len(efficiency))
    avg_complexity = sum(complexity)/ float(len(complexity))
    # list_json = json.dumps(list_benchmark)
    average = [avg_bleeding, avg_efficiency, avg_complexity]
    print (average)
    list_avg = json.dumps(average)
    print (list_avg)
    cur.close()
    connection.close()
    return list_avg

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5000)