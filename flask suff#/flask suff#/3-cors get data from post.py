import sqlite3
from flask import Flask, redirect, url_for, request, jsonify, make_response, current_app
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})



@app.route('/print', methods=['GET', 'POST'])
def printTest():
    content = request.json
    #print(content)
    print(content["ID"])
    return content["ID"] 
   
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
