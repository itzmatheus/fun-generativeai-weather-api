from fastapi.testclient import TestClient
from main import app
from src.generativeai import GenerativeAIText, get_chatgpt_generative_ai_text

client = TestClient(app)

class MockGenerativeAIText(GenerativeAIText):
    def generate_text(self, prompt: str, system_prompt: str = None, max_tokens: int = 200):
        return f"Generated text mock"
    
def override_get_chatgpt_generative_ai_text() -> GenerativeAIText:
    return MockGenerativeAIText()

app.dependency_overrides[get_chatgpt_generative_ai_text] = override_get_chatgpt_generative_ai_text

def test_should_generate_question_success():
    response = client.post("/city/question_generate", json={"entrada": "Pianco"})
    
    assert response.status_code == 200
    assert response.json() == {"saida": "Generated text mock"}