class WeatherDTO:
    def __init__(self, description: str): 
        self.description: str = description

    @classmethod
    def from_dict(cls, data: dict):
        description = data.get("current_condition")[0].get("lang_pt")[0].get("value")
        return cls(description)