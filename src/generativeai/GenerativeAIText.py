from abc import ABC, abstractmethod

class GenerativeAIText(ABC):

    @abstractmethod
    def generate_text(self, prompt: str, system_prompt: str = None, max_tokens: int = 200) -> str:
        pass