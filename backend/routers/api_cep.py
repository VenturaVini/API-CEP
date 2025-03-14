import requests
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/cep/{cep}")
def get_cep(cep: str):
    if len(cep) != 8 or not cep.isnumeric():
        raise HTTPException(status_code=400, detail="CEP inválido")
    url = f'https://viacep.com.br/ws/{cep}/json'
    requisicao = requests.get(url)
    return requisicao.json()