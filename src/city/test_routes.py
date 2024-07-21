from fastapi.testclient import TestClient
from main import app
from src.generativeai import GenerativeAIText, get_chatgpt_generative_ai_text
from src.weather import WeatherApi, get_wttr_weather_api, WeatherDTO

client = TestClient(app)

class MockGenerativeAIText(GenerativeAIText):
    def generate_text(self, prompt: str, system_prompt: str = None, max_tokens: int = 200):
        return f"Generated text mock"

def override_get_chatgpt_generative_ai_text() -> GenerativeAIText:
    return MockGenerativeAIText()    

class MockGenerativeAITextFailure(GenerativeAIText):
    def generate_text(self, prompt: str, system_prompt: str = None, max_tokens: int = 200):
        raise Exception("Generative AI failure")

def override_generativeai_text_failure() -> GenerativeAIText:
    return MockGenerativeAITextFailure()    

class MockWeatherApi(WeatherApi):
    def get_weather(self, location: str) -> str:
        return WeatherDTO(description="Sunny")
    
def override_get_wttr_weather_api() -> WeatherApi:
    return MockWeatherApi()

class MockWeatherApiFailure(MockWeatherApi):
    def get_weather(self, location: str):
        raise Exception("Weather API failure")

def override_get_wttr_weather_api_failure() -> WeatherApi:
    return MockWeatherApiFailure()

def test_should_generate_question_success():
    app.dependency_overrides[get_chatgpt_generative_ai_text] = override_get_chatgpt_generative_ai_text
    app.dependency_overrides[get_wttr_weather_api] = override_get_wttr_weather_api

    response = client.post("/city/question_generate", json={"entrada": "Pianco"})
    
    assert response.status_code == 200
    assert response.json() == {"saida": "Generated text mock"}

def test_shouldnt_generate_question_when_weather_api_fails():    
    app.dependency_overrides[get_wttr_weather_api] = override_get_wttr_weather_api_failure

    response = client.post("/city/question_generate", json={"entrada": "Pianco"})
    
    assert response.status_code == 500
    assert response.json() == {"detail": "Weather API failure"}

def test_shouldnt_generate_question_when_generative_ai_fails():
    app.dependency_overrides[get_wttr_weather_api] = override_get_wttr_weather_api
    app.dependency_overrides[get_chatgpt_generative_ai_text] = override_generativeai_text_failure

    response = client.post("/city/question_generate", json={"entrada": "Pianco"})
    
    assert response.status_code == 500
    assert response.json() == {"detail": "Generative AI failure"}