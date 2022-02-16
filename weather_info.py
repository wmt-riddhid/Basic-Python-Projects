from email.mime import base
import requests
from pprint import pprint # it will give response in a JSON format

API_Key = "86df455fdc0e379cea72255a8b391857"

city = input("Enter a city : ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" +API_Key+ "&q=" +city

weather_data = requests.get(base_url).json()

pprint(weather_data)

# in output :=
# clouds - will gives you coordinates (latitudes, longitudes)
# 