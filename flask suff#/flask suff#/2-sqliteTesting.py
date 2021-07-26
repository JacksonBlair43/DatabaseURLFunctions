import requests
##url = 'http://127.0.0.1:5000/getmessages'
##data = {"ID": "1"}
##r = requests.post(url,  verify=False, json=data)
requests.get()
 
from requests.exceptions import HTTPError

for url in ['http://127.0.0.1:5000/getmessages?data=%7B%22ID%22%3A%20%222%22%7D']:
    try:
        response = requests.get(url)

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')
