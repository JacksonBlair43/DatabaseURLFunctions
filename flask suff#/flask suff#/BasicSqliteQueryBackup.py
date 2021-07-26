import sqlite3
import json
from flask import Flask, redirect, url_for, request, jsonify
app = Flask(__name__)


@app.route('/getmessages', methods=['GET', 'POST'])
def getmessages():
    content = request.args.get('data')
    ##content = request.json
    print(content)
    content2 = json.loads(content)
    res = get(content2["ID"])
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
