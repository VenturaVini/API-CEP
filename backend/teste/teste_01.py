import requests

url = f'https://viacep.com.br/ws/50940230/json'


requisicao = requests.get(url)
print(requisicao.json())