from openai import OpenAI

from src.generativeai import GenerativeAIText
from src.config.settings import OPEN_AI_KEY

class ChatGPTGenerativeAIText(GenerativeAIText):

    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)
        self.model = "gpt-3.5-turbo"

    def generate_text(self, prompt: str, system_prompt: str = None, max_tokens: int = 200) -> str:

        messages = [{"role": "user", "content": prompt}]

        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            max_tokens=max_tokens)
        
        return response.choices[0].message.content.strip()

def get_chatgpt_generative_ai_text() -> GenerativeAIText:
    return ChatGPTGenerativeAIText(OPEN_AI_KEY)