import json
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/test/<number>")
def home():
    number = None
    if number == 1:
        url = 'http://127.0.0.1:5000/query_records'
        data = {"ID": "1"}
        r = requests.get(url, params={"json": data})
        return r.text
    elif number == 2:
        url = 'http://127.0.0.1:5000/create_record'
        data = {"ID": "1"}
        r = requests.post(url,  verify=False, json=data)
        return r.text
    elif number == 3:
        url = 'http://127.0.0.1:5000/update_record'
        data = {"ID": "1"}
        r = requests.put(url,  verify=False, json=data)
        return r.text
    url = 'http://127.0.0.1:5000/delete_record'
    data = {"ID": "1"}
    r = requests.delete(url,  verify=False, json=data)
    return r.text

@app.route('/query_records', methods=['GET'])
def query_records():
    name = request.args.get('name')
    print(name)
    with open('/tmp/data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for record in records:
            if record['name'] == name:
                return jsonify(record)
        return jsonify({'error': 'data not found'})

@app.route('/create_record', methods=['PUT'])
def create_record():
    record = json.loads(request.data)
    with open('/tmp/data.txt', 'r') as f:
        data = f.read()
    if not data:
        records = [record]
    else:
        records = json.loads(data)
        records.append(record)
    with open('/tmp/data.txt', 'w') as f:
        f.write(json.dumps(records, indent=2))
    return jsonify(record)

@app.route('/update_record', methods=['POST'])
def update_record():
    record = json.loads(request.data)
    new_records = []
    with open('/tmp/data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
    for r in records:
        if r['name'] == record['name']:
            r['email'] = record['email']
        new_records.append(r)
    with open('/tmp/data.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)
    
@app.route('/delete_record', methods=['DELETE'])
def delte_record():
    record = json.loads(request.data)
    new_records = []
    with open('/tmp/data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for r in records:
            if r['name'] == record['name']:
                continue
            new_records.append(r)
    with open('/tmp/data.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)

app.run()
