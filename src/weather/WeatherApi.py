from abc import ABC, abstractmethod
from .WeatherDTO import WeatherDTO

class WeatherApi(ABC):

    @abstractmethod
    def get_weather(self, location: str) -> WeatherDTO:
        pass