import requests

URL = "https://wttr.in/{city}?format=j1"

def get_weather(city: str) -> str:
    response = requests.get(URL.format(city=city))
    return response.json().get("current_condition")[0].get("weatherDesc")[0].get("value")