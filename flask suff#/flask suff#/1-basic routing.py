import json
from flask import Flask
app = Flask(__name__)

@app.route('/alice')
def indexalice():
    return json.dumps({'name': 'alice',
                       'email': 'alice@outlook.com'})

@app.route('/bob')
def indexbob():
    return json.dumps({'name': 'bob',
                       'email': 'bob@outlook.com'})

app.run()
