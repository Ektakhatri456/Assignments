# Weather Program Python project

import requests
from pprint import pprint

API_key = '1ab87db3cde3e6e85114b94426352dd4'
city = input("Enter a city: ")
base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_key + "&q=" + city

weather_data = requests.get(base_url).json()
pprint(weather_data)


