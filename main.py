from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/precos")
def consultar_precos(data: str):
    try:
        resposta = requests.get("https://testedefensoriapr.pythonanywhere.com/precos")
        resposta.raise_for_status()

        return {
            "data_informada": data,
            "precos": resposta.json()
        }

    except requests.exceptions.RequestException:
        return {
            "erro": "Não foi possível consultar a API externa no momento."
        }