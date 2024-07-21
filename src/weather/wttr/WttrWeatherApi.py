import requests

from src.weather import WeatherApi, WeatherDTO

class WttrWeatherApi(WeatherApi):

    def __init__(self):
        self.url = "https://wttr.in"

    def get_weather(self, location: str) -> WeatherDTO:
        response = requests.get(f"{self.url}/{location}?format=j1&lang=pt")
        return WeatherDTO.from_dict(response.json())

def get_wttr_weather_api() -> WeatherApi:
    return WttrWeatherApi()