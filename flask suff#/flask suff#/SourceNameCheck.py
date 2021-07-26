from flask import Flask, request
appFlask = Flask(__name__)


# http://127.0.0.1:5000/index?source=test
@appFlask.route('/index')
def access_param():
    source = request.args.get('source')
    return '''<h1>The source value is: {}</h1>'''.format(source)
appFlask.run(debug=False, port=5000)
