from pydantic import BaseModel

class CityRequest(BaseModel):
    entrada: str


class CityResponse(BaseModel):
    saida: str