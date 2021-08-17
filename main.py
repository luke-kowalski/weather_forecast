import requests

api = "3af3d3b40ec932ed51b8c87bfecc03d6"
lat = 53.216198
lon = 19.654487

url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=metric&exclude=hourly,minutely&appid={api}"



response = requests.get(url)
jsonResponse = response.json()


print(url)
print(jsonResponse['daily'])

for days in jsonResponse['daily']:
    print(days['dt'])
