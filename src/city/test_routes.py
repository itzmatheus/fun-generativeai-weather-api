from fastapi.testclient import TestClient
from main import app
from src.generativeai import GenerativeAIText, get_chatgpt_generative_ai_text
from src.weather import WeatherApi, get_wttr_weather_api

client = TestClient(app)

class MockGenerativeAIText(GenerativeAIText):
    def generate_text(self, prompt: str, system_prompt: str = None, max_tokens: int = 200):
        return f"Generated text mock"
    
class MockWeatherApi(WeatherApi):
    def get_weather(self, location: str) -> str:
        return "Sunny"
    
def override_get_chatgpt_generative_ai_text() -> GenerativeAIText:
    return MockGenerativeAIText()

def override_get_wttr_weather_api() -> WeatherApi:
    return MockWeatherApi()

app.dependency_overrides[get_chatgpt_generative_ai_text] = override_get_chatgpt_generative_ai_text
app.dependency_overrides[get_wttr_weather_api] = override_get_wttr_weather_api

def test_should_generate_question_success():
    response = client.post("/city/question_generate", json={"entrada": "Pianco"})
    
    assert response.status_code == 200
    assert response.json() == {"saida": "Generated text mock"}