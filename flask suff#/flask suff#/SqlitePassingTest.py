import sqlite3
import requests
from flask import Flask, redirect, url_for, request, jsonify
app = Flask(__name__)

@app.route("/test")
def home():
    url = 'http://127.0.0.1:5000/getmessages'
    data = {"ID": "3"}
    r = requests.post(url,  verify=False, json=data)
    return r.text

@app.route('/getmessages', methods=['GET', 'POST'])
def getmessages():
    content = request.json
    print(content)
    res = get(content["ID"])
    return res


def get(ID):
    connection = sqlite3.connect('testDB.db')
    c = connection.cursor()
    c.execute("SELECT * FROM messages where ID =  "+ID+";")
    rows = c.fetchall()
    if(len(rows) !=0):
        print(rows)
        return {"rows":rows}
    else:
        return {"rows":[]}


   
 
if __name__ == '__main__':
    app.run(debug = True)
    ##app.run(host='0.0.0.0', port=80)
