from time import sleep
import pyautogui

email = 'rafael_lucen@hotmail.com '


log = open(r"C:\Users\USER\Desktop\dados_rafa\login.txt", "r")
login = log.read()
senha = login

    
def inicia_live():
    try:
        chrome = 'chrome.png'
        pyautogui.click(chrome)
    except:
        chrome = 'chrome2.png'
        pyautogui.click(chrome)
    sleep(2)
    
    print('error2')
    pyautogui.click(600, 600)
    print('error1')
    pyautogui.write('https://www.youtube.com/')
    pyautogui.press(['Enter'])
    sleep(3)
    pyautogui.click('./abrir_tela.png')
    
    print('erro3')
    #write para escrever os codigos
    print('error')
    try:
        sleep(2)
        pyautogui.click(1210, 100)
        sleep(0.5)
    except:
        pyautogui.click(1210, 380)
    try:
        pyautogui.click('./perfil.png')
    except:
        pyautogui.click('./my_perfil.png')
    
    
    

   
inicia_live()