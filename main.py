import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv('.env')

api_token = os.getenv('API_TOKEN')
lat = 53.216198
lon = 19.654487

url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=metric&exclude=hourly,minutely&appid={api_token}"


response = requests.get(url)
jsonResponse = response.json()


for days in jsonResponse["daily"]:
    print(datetime.fromtimestamp(int(days["dt"])).strftime("%Y,%m,%d"))
    print(days["dt"])
    print(datetime.fromtimestamp(int(days["sunrise"])).strftime("%H:%M:%S"))
    print(datetime.fromtimestamp(int(days["sunset"])).strftime("%H:%M:%S"))
    print(days["temp"]["day"])
    print(days["temp"]["night"])
    print(days["pressure"])
    print(days["humidity"])
    print((days["weather"][0]["main"] + " - " + days["weather"][0]["description"]))
