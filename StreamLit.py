import requests
import json 


url = 'http://127.0.0.1:8000/mine_block/'

myobj = {'data': 'somevalue'}

json_object = json.dumps(myobj, indent = 4) 

x = requests.post(url, data = json_object)
print(x.text)