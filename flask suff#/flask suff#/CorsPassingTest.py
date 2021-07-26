import sqlite3
import requests
from flask import Flask, redirect, url_for, request, jsonify, make_response, current_app
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/test")
def home():
    import requests
    url = 'http://127.0.0.1:5000/print'
    data = {"ID": "1"}
    r = requests.post(url,  verify=False, json=data)
    print("Status code is " + str(r.status_code))
    return str(r.status_code)

@app.route('/print', methods=['GET', 'POST'])
def printTest():
    content = request.json
    #print(content)
    print(content["ID"])
    return content["ID"] 
   
 
if __name__ == '__main__':
    app.run(debug = True)
    ##app.run(host='0.0.0.0', port=80)
