import requests
url = 'http://127.0.0.1:5000/getmessages'
data = {"ID": "1"}
r = requests.post(url,  verify=False, json=data)

 
 
