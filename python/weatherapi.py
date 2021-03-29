import json
import requests

print('Please enter your city: ')
city = input()
r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=%s&appid=ff49736f1e05b1054389059b3097fac3' % city)
data = r.json()

print("The weather in %s is: "%city +data['weather'][0]['description'] )
#dictionaries are in { } and use key value pairs
#lists are in [ ]  and use numeric indexes [0-n]