import requests
from deep_translator import GoogleTranslator


def obter_clima_cidade(cidade: str, token: str = '72c4ae5b5e5d07b13944a5e8e0387782'):


    url = f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={token}&lang=pt_br&units=metric'
    requisicao = requests.get(url)  

    if requisicao.status_code != 200:
        return {'erro': 'Cidade não encontrada'} 

    clima = {}

    clima['temperatura'] = requisicao.json()['main']['temp']
    clima['sensacao_termica'] = requisicao.json()['main']['feels_like']
    clima['temperatura_minima'] = requisicao.json()['main']['temp_min']
    clima['temperatura_maxima'] = requisicao.json()['main']['temp_max']
    clima['umidade'] = requisicao.json()['main']['humidity']
    
    try:
        estado_atual = requisicao.json()['weather'][0]['main']
        estado_traduzido = GoogleTranslator(source="en", target="pt").translate(estado_atual)
        clima['estado_atual'] = estado_traduzido
    except:       
        clima['estado_atual'] = requisicao.json()['weather'][0]['main']

    clima['descricao'] = requisicao.json()['weather'][0]['description']
    
    return clima


print(obter_clima_cidade('São Paulo'))


