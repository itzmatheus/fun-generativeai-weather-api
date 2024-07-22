from openai import OpenAI

from src.generativeai import GenerativeAIText
from src.config.settings import LM_STUDIO_MODEL, LM_STUDIO_API_KEY, LM_STUDIO_BASE_URL

class DolphinGenerativeAIText(GenerativeAIText):
    
    def __init__(self, api_key: str, base_url: str, model: str):
        self.client = OpenAI(api_key=api_key, base_url=base_url)
        self.model = model

    def generate_text(self, prompt: str, system_prompt: str = None, max_tokens: int = 200) -> str:
        messages = [{"role": "user", "content": prompt}]

        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            max_tokens=max_tokens)
        
        return response.choices[0].message.content.replace('\\"', '').strip()

def get_dolphin_generative_ai_text() -> GenerativeAIText:
    return DolphinGenerativeAIText(api_key=LM_STUDIO_API_KEY, base_url=LM_STUDIO_BASE_URL, model=LM_STUDIO_MODEL)