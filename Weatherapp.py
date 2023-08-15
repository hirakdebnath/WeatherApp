import requests
import json
import os

entr=f" say Enter a City"
os.system(entr)
city= input("Enter the name of the city:")

url=f"http://api.weatherapi.com/v1/current.json?key=32c98be0540a4a429e7155959232207&q={city}&aqi=yes"

r=requests.get(url)
# print(r.text)
weatherdic=json.loads(r.text)
print(weatherdic["current"]["temp_c"])

temp=weatherdic["current"]["temp_c"]

command=f" say The temparature at {city} is {temp} degree celcius"
os.system(command)

