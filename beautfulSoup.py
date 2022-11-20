from unicodedata import name
from bs4 import BeautifulSoup
import requests


page = requests.get("http://pcdsh01.on.br/HoraLegalBrasileira.php")#https://relogioonline.com.br/horario/bras%C3%ADlia/ 

soup = BeautifulSoup(page.text, 'html.parser')

artist_name_list_hora = soup.find(id='lbl-time')
artist_name_list_data = soup.find(id='cityClock')
print(artist_name_list_data)
# for c in artist_name_list_data:

#     hora = c.contents[0]
#     print(hora)

