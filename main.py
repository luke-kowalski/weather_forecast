import requests
from datetime import datetime
from configparser import ConfigParser

parser = ConfigParser()
parser.read("config.ini")
api_token = parser.get("WEATHER_API", "api_token")


class IncorrectResponseStatus:
    def __init__(self, code_recieved):
        msg = f"code_recieved: {code_recieved}"
        super().__init__(msg)


class GetWheatherData:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        self.url = f"https://api.openweathermap.org/data/2.5/onecall?lat={self.lat}&lon={self.lon}&units=metric&exclude=hourly,minutely&appid={api_token}"

    def _get_response_dict(self):
        response = requests.get(self.url)
        if response.status_code != 200:
            raise IncorrectResponseStatus(response.status_code)
        return response.json()

    def _get_html_elements(self):
        response = self._get_response_dict()
        html_elements = []
        for days in response["daily"]:
            wf_day = datetime.fromtimestamp(int(days["dt"])).strftime("%Y-%m-%d")
            wf_sunrise = datetime.fromtimestamp(int(days["sunrise"])).strftime(
                "%H:%M:%S"
            )
            wf_sunset = datetime.fromtimestamp(int(days["sunset"])).strftime("%H:%M:%S")
            wf_temp_day = days["temp"]["day"]
            wf_temp_night = days["temp"]["night"]
            wf_pressure = days["pressure"]
            wf_humidity = days["humidity"]
            wf_description = (
                days["weather"][0]["main"]  + " - " + days["weather"][0]["description"]
            )
            html_div = f"{wf_day}  <br>  {wf_description}  <br>  {wf_temp_day}  <br>  {wf_temp_night}  <br>  {wf_sunrise}  <br>  {wf_sunset}  <br>  {wf_pressure}  <br>  {wf_humidity}"
            html_elements.append(html_div)
        return html_elements

    def get_html(self):
        elements = self._get_html_elements()
        return "\n".join(elements)        

    def save_html_to_file(self):
        try:
            myfile = open("index.html", "w")
        except PermissionError:
            input("Please close file: index.html")
            myfile = open("index.html", "w")
        myfile.write(self.get_html())
        myfile.close()
        print(self.get_html())


fialki = GetWheatherData(53.216198, 19.654487)

fialki.save_html_to_file()
