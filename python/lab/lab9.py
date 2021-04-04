import json
import requests


r = requests.get('http://localhost:3000')

data = r.json()

for i in data:
    print(i['name'] + " is " + i['color'])



#dictionaries are in { } and use key value pairs
#lists are in [ ]  and use numeric indexes [0-n]