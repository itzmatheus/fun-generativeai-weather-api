from fastapi import APIRouter, HTTPException

from .schemas import CityRequest, CityResponse

from src.openai import open_ai_client

city_router = APIRouter(prefix="/city", tags=["city"])

@city_router.post("/question_generate")
def question_generate(request: CityRequest) -> CityResponse:
    try:
        
        system_prompt = f"""
            Voce ira gerar um breve texto divertido a partir do clima atual e nome da cidade, e apenas isso.
        """

        prompt = f"""
            Gere o texto com base nos seguintes dados:
            - Nome da cidade: {request.entrada}
            - Clima atual: calor
            - Tom: divertido
        """

        response = open_ai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ], max_tokens=200)

        generated_text = response.choices[0].message.content.strip()
        return CityResponse(saida=generated_text)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))