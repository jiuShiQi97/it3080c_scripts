import json
import requests


r = requests.get('https://wenhanja.herokuapp.com/api')

data = r.json()

for i in data:
    print(i['name'] + " is " + i['color'])
