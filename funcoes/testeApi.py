import requests
import json
def buscar_dados():
    request = requests.get("http://worldtimeapi.org/api/timezone/America/Sao_Paulo")
    todos = json.loads(request.content)
    print(todos['datetime'])
#https://www.treinaweb.com.br/blog/consumindo-apis-com-python-parte-1
buscar_dados()