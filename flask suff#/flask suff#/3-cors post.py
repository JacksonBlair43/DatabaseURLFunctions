import requests
url = 'http://127.0.0.1:80/print'
data = {"ID": "1"}
r = requests.post(url,  verify=False, json=data)
print(r.status_code)

 
