import sqlite3
import json
import requests
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/Input')
def input():
    return render_template("InputForm.html")

@app.route('/getmessages', methods=['GET', 'POST'])
def getmessages():
    content = requests.get(request.json)
    print(content)
    res = get(content["ID"])
    return res

#@app.route('/getmessages',)
#    def getmessages():
#    content = {"ID": "1"}
#    print(content)
#    res = get(content["ID"])
#    return res


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
##if __name__ == '__main__':
##    app.run(host='0.0.0.0', port=80)
