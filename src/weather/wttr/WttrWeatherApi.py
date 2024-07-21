import requests

from src.weather import WeatherApi

class WttrWeatherApi(WeatherApi):

    def __init__(self):
        self.url = "https://wttr.in"

    def get_weather(self, location: str) -> str:
        response = requests.get(f"{self.url}/{location}?format=j1&lang=pt")
        return response.json().get("current_condition")[0].get("lang_pt")[0].get("value")

def get_wttr_weather_api() -> WeatherApi:
    return WttrWeatherApi()