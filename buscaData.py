import requests
import json
from datetime import datetime

def dataAtualWeb():
    request = requests.get("http://worldtimeapi.org/api/timezone/America/Sao_Paulo")
    tudo = json.loads(request.content)
    data = tudo['datetime']
    data_certa = data[0:10]
    date = datetime.strptime(data_certa, '%Y-%m-%d').date()
    
    return date.strftime('%A')

print(dataAtualWeb())