from fastapi import APIRouter, Depends, HTTPException

from .schemas import CityRequest, CityResponse
from src.weather import get_weather

from src.generativeai import GenerativeAIText, get_chatgpt_generative_ai_text

city_router = APIRouter(prefix="/city", tags=["city"])

@city_router.post("/question_generate")
def question_generate(
    request: CityRequest,
    generativeai_text: GenerativeAIText = Depends(get_chatgpt_generative_ai_text)
    ) -> CityResponse:
    try:
        
        weather = get_weather(request.entrada)

        system_prompt = f"""
            Voce ira gerar um breve texto divertido a partir do clima atual e nome da cidade, e apenas isso.
        """

        prompt = f"""
            Gere o texto com base nos seguintes dados:
            - Nome da cidade: {request.entrada}
            - Clima atual: {weather}
            - Tom: divertido
        """

        generated_text = generativeai_text.generate_text(prompt=prompt, system_prompt=system_prompt)

        return CityResponse(saida=generated_text)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))