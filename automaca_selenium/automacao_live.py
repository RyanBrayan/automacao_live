from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


navegador = webdriver.Chrome(r'C:\Users\USER\Desktop\arquivo\chromedriver.exe')
email = 'sedutorryan@gmail.com'
senha = ''


#Entrar no youtube e ir para parte de live
def login(email, senha):
    navegador.get("https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Dpt%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=pt-BR&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    barra = navegador.find_element_by_xpath('//*[@id="identifierId"]')
    sleep(3)
    barra.send_keys(email)
    barra.send_keys(Keys.ENTER)
    sleep(3)
    
    
def live():
    
    barra_pesquisa = navegador.find_element_by_xpath('//*[@id="button"]')
    barra_pesquisa.click()

login(email, senha)