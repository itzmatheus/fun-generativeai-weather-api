from abc import ABC, abstractmethod

class WeatherApi(ABC):

    @abstractmethod
    def get_weather(self, location: str) -> str:
        pass