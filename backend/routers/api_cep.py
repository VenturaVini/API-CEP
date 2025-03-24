import requests
from fastapi import APIRouter, HTTPException
from deep_translator import GoogleTranslator
import telebot
from services.api_frases_aleatorias import obter_frase_aleatoria



def enviar_mensagem(mensagem, CHAT_ID = '5588207726',BOT_TOKEN = '7294948712:AAEj57qIFRaXmS8ZB__0nq6SETufOIb6hzQ'):

    bot = telebot.TeleBot(BOT_TOKEN)

    # Enviando a mensagem
    bot.send_message(CHAT_ID, mensagem)

router = APIRouter()



def obter_clima_cidade(cidade: str, token: str = '72c4ae5b5e5d07b13944a5e8e0387782'):


    url = f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={token}&lang=pt_br&units=metric'
    requisicao = requests.get(url)  

    if requisicao.status_code != 200:
        return {'erro': 'Cidade não encontrada'} 

    clima = {}

    clima['temperatura'] = round(requisicao.json()['main']['temp'])
    clima['sensacao_termica'] = round(requisicao.json()['main']['feels_like'])
    clima['temperatura_minima'] = round(requisicao.json()['main']['temp_min'])
    clima['temperatura_maxima'] = round(requisicao.json()['main']['temp_max'])
    clima['umidade'] = round(requisicao.json()['main']['humidity'])
    
    try:
        estado_atual = requisicao.json()['weather'][0]['main']
        estado_traduzido = GoogleTranslator(source="en", target="pt").translate(estado_atual)
        clima['estado_atual'] = estado_traduzido
    except:       
        clima['estado_atual'] = requisicao.json()['weather'][0]['main']

    clima['descricao'] = requisicao.json()['weather'][0]['description'].title()
    
    return clima


@router.get("/cep/{cep}")
def get_cep(cep: str):
    if len(cep) != 8 or not cep.isnumeric():
        raise HTTPException(status_code=400, detail="CEP inválido")
    url = f'https://viacep.com.br/ws/{cep}/json'
    requisicao = requests.get(url)

    complemento_api_clima = obter_clima_cidade(requisicao.json()["localidade"])

    dados_cep = requisicao.json()

    frase_aleatoria = obter_frase_aleatoria()

    # adicionar os dados do clima na requisicao do cep
    dados_cep.update(complemento_api_clima)

    dados_cep.update({'frase_aleatoria': frase_aleatoria})

    # enviar_mensagem(f'CEP {cep} consultado: Rua {requisicao.json()["logradouro"]}, Bairro {requisicao.json()["bairro"]}, Cidade {requisicao.json()["localidade"]}, Estado {requisicao.json()["uf"]}')
    enviar_mensagem(
    f"CEP {cep}\n"
    f"Rua: {dados_cep.get('logradouro', 'Não disponível')}\n"
    f"Bairro: {dados_cep.get('bairro', 'Não disponível')}\n"
    f"Cidade: {dados_cep.get('localidade', 'Não disponível')}\n"
    f"Estado: {dados_cep.get('uf', 'Não disponível')}\n"

    f"\n"
    f"Clima Atual: {dados_cep.get('estado_atual', 'Não disponível')}\n"
    f"Descrição: {dados_cep.get('descricao', 'Não disponível')}\n"
    f"Temperatura: {dados_cep.get('temperatura', 'Não disponível')}\n"

    f"\n"
    f"Frase Aleatória: {dados_cep.get('frase_aleatoria', 'Não disponível')}"
    )   

    return dados_cep



