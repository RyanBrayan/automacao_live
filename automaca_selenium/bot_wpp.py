from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import time
from time import sleep

'''
Basicamente um programa que busca a temperatura da sua cidade
e noticias do G1 e envia para algum contato em especifico por 
whatsapp.
'''

navegador = webdriver.Chrome(r'C:\Users\USER\Desktop\arquivo\chromedriver.exe')

guardar_temperatura = []
guardar_noticias = []

cookie = {'name' : 'tok', 
          'value' : '1@LCfz5mWxkHPNwqQ+FUMFjHIKVMI/M5DqVCZu6rmAS9UwH7qqFa9yi8hhFizKnnVUV2j2tGgM7gYiVg==', 
          'path':'/pp','secure':True }
cookie = {'name' : 'ref', 
          'value' : '1@NuSW5ZboeocCnZNwJLekpkYEhn7CmQwo4vWx5nCeiXQte+X7S73bkJkSi4WpXjx8/xfXE3ymGcLJ5w==', 
          'path':'/pp','secure':True }

#Definindo os contatos para enviar a temperatura e informações. 
contatos = ['Filho Ryan']#adicione o nome do contato corretamente ex: "Contato".




def buscar_temp():
    #Abrindo o chrome
    navegador.get('https://www.google.com.br/')
    barra_pesquisa = navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    barra_pesquisa.click()
    #Buscando a temperatura 
    barra_pesquisa.send_keys('Temperatura franco da rocha ') #Coloque o nome da sua cidade 
    sleep(2)
    barra_pesquisa.send_keys(Keys.ENTER)
    #Pegando temperatura
    temperatura = navegador.find_element_by_xpath('//*[@id="wob_tm"]')
    guardar_temperatura.append(temperatura.text)
    sleep(2)


def buscando_noticias():
    #Vai ir até o navegador e buscar por noticias do G1-Globo
    navegador.get('https://g1.globo.com/sp/sao-paulo/')
    sleep(5)
    noticias = navegador.find_element_by_class_name('_evt')
    
    guardar_noticias.append(noticias.text)
    print(guardar_noticias)
    for noticias in guardar_noticias:
        return f'Noticias G1\n\n{noticias}'


def buscar_contato(contato):
    navegador.get('https://web.whatsapp.com')
    sleep(40) #Tempo para scanear o QR CODE do Whatsapp
    navegador.add_cookie(cookie)
    navegador.get_cookies()
    campo_pesquisa = navegador.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    sleep(4)
    #Vai buscar os contatos 
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)
    sleep(2)
    

def enviar_mensagem(*mensagem):
    #vai enviar as mensagens a pessoa
    
    
    campo_mensagem = navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]') 
    campo_mensagem.click()
    sleep(3)
    while True:
        hora = time.minute
        if hora == 20:
            break
    campo_mensagem.send_keys(mensagem)
    campo_mensagem.send_keys(Keys.ENTER)
    sleep(3)
    navegador.quit()
    

mensagens = []
def chama_funcoes():
    #chamando as funçoes 
    #buscar_temp()
    #noticia = buscando_noticias()
    mensagem = f'Feliz ano novo familia e um prospero ano novo para todos vocês!!!!!! Que de tudo certo na vida de vocês. Meus amigos, que nesta virada de ano possam olhar para trás e louvar a Deus por todas as bênçãos recebidas. Assim como agradecer cada vitória conquistada e cada obstáculo superado :)'
    #mensagens.append(noticia)
    mensagens.append(mensagem)
    
    #pegando os contatos da lista e enviando as mensagens 
    for contato in contatos:
        buscar_contato(contato)
        for mens in mensagens:
            enviar_mensagem(mens)
            sleep(5)
            try:
                alerta = navegador.switch_to.alert
                alerta.accept()
            except:
                continue
cont = 0

while True: #tempo que o codigo vai rodar
    chama_funcoes()
    cont += 1
    if cont == 4: #quantas vezes o programa vai enviar as mensagens
        break
    sleep(900) #de quanto, em quanto tempo ele vai envair as mensagens. Pré definido 15 minutos