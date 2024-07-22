class WeatherDTO:
    def __init__(self, description: str): 
        self.description: str = description

    @classmethod
    def from_dict(cls, data: dict):
        description = data.get("current_condition")[0].get("weatherDesc")[0].get("value")
        return cls(description)