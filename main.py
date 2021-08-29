import requests
from datetime import datetime
from configparser import ConfigParser

parser = ConfigParser()
parser.read('config.ini')

api_token = parser.get('WEATHER_API', 'api_token')

lat = 53.216198
lon = 19.654487

url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=metric&exclude=hourly,minutely&appid={api_token}"


response = requests.get(url)
jsonResponse = response.json()


for days in jsonResponse["daily"]:
    wf_day = datetime.fromtimestamp(int(days["dt"])).strftime("%Y-%m-%d")
    wf_sunrise = datetime.fromtimestamp(int(days["sunrise"])).strftime("%H:%M:%S")
    wf_sunset = datetime.fromtimestamp(int(days["sunset"])).strftime("%H:%M:%S")
    wf_temp_day = days["temp"]["day"]
    wf_temp_night = days["temp"]["night"]
    wf_pressure = days["pressure"]
    wf_humidity = days["humidity"]
    wf_description = (days["weather"][0]["main"] + " - " + days["weather"][0]["description"])

    print(wf_day)
    print(wf_sunrise)
    print(wf_sunset)
    print(wf_temp_day)
    print(wf_temp_night)
    print(wf_pressure)
    print(wf_humidity)
    print(wf_description)