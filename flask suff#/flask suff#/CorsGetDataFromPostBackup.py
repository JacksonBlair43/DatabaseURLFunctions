import sqlite3
import json
from flask import Flask, redirect, url_for, request, jsonify, make_response, current_app
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/print', methods=['GET', 'POST'])
def printTest():
    content = request.args.get('data')
    ##content = request.json
    print(content)
    content2 = json.loads(content)
    print(content2["ID"])
    return content2["ID"] 
   
 
if __name__ == '__main__':
    app.run(debug = True)
    ##app.run(host='0.0.0.0', port=80)
