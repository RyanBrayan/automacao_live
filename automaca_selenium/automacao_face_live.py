
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import alert_is_present
import pyautogui

navegador = webdriver.Chrome(r'C:\Users\USER\Desktop\arquivo\chromedriver.exe')

email = 'rafael_lucen@hotmail.com '


log = open(r"C:\Users\USER\Desktop\dados_rafa\login.txt", "r")
login = log.read()
senha = login

navegador.get('https://www.facebook.com/')
wdw = WebDriverWait(navegador, 30)


def login_facebook(email, senha):
    login_email = navegador.find_element_by_id('email')
    login_email.click()
    
    login_email.send_keys(email)
    
    login_senha = navegador.find_element_by_id('pass')
    login_senha.click()
    
    login_senha.send_keys(senha)
    
    login_senha.send_keys(Keys.ENTER)
    sleep(5)
    
    
def inicia_live():
    navegador.get('https://www.facebook.com/live/producer/v2/?entry_point=feedx_sprouts&target_id=100007217952954')
    sleep(4)
    pyautogui.click(150, 300)
    selecionar = 'selecionar.png' 
    pyautogui.click(selecionar) #aperta no botao selecionar 
    sleep(4)
    fecha_ajuda =  'x.png'
    sleep(3)
    
    for c in range(0, 2):
        try:
            pyautogui.click(fecha_ajuda, clicks=2, interval=1) #vai procura pelo botao de fechar ajuda 
            sleep(0.5)
        except:
            continue
        
    copy_chave = 'salvar.png'
    pyautogui.click(copy_chave)
    #parte que vai colar no obs a chave de streaming
    #pyautogui.keyDown(['ctrl'])
    #pyautogui.press(['v'])
    #pyautogui.keyUp(['ctrl'])
    #PEGAR A CHAVE DA URL 
    sleep(1)
    
    seta_mais_opcoes = 'seta.png'
    pyautogui.click(seta_mais_opcoes)#mostra mais opcoes
    pyautogui.press(['end']) #vai ate o final da page
    sleep(2)
    copy_url = 'salvar_url.png'
    pyautogui.click(copy_url) #copia a url de streaming
    

   
login_facebook(email, senha)
inicia_live()