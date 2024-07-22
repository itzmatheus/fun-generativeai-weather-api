from src.config.settings import USE_EXTERNAL_GEN_AI
from .GenerativeAIText import GenerativeAIText
from .lmstudio.DolphinGenerativeAIText import get_dolphin_generative_ai_text
from .openai.ChatGPTGenerativeAIText import get_chatgpt_generative_ai_text

def get_generativeai_text_factory() -> GenerativeAIText:
    if USE_EXTERNAL_GEN_AI:
        return get_chatgpt_generative_ai_text()
    return get_dolphin_generative_ai_text()