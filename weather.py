import requests
import pandas as pd
import json
from matplotlib import pyplot as plt

#zip_code = input("Enter zip code")

api_key = '93a2195c80msh73fbe80a2f75999p1122a4jsn873f512f5d5d'

url = "https://community-open-weather-map.p.rapidapi.com/forecast"

querystring = {"q":"omaha,us","units":"imperial"}

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "93a2195c80msh73fbe80a2f75999p1122a4jsn873f512f5d5d"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

with open("weather.json", "w") as f:
   f.write(response.text)

with open("weather.json") as f:
   json_weather = json.load(f)

temps = []

for i in range(json_weather['cnt']):
    temps.append(json_weather['list'][i]['main']['temp'])

x = range(json_weather['cnt'])
y = temps

plt.plot(x, y)
plt.show()