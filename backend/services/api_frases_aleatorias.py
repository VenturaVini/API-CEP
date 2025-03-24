import requests
from deep_translator import GoogleTranslator


def obter_frase_aleatoria():
    url = 'https://zenquotes.io/api/random'
    requisicao = requests.get(url)
    texto = requisicao.json()[0]['q']
    tradutor_texto = GoogleTranslator(source="en", target="pt").translate(texto)
    return tradutor_texto

print(obter_frase_aleatoria())