from time import sleep
import pyautogui

email = 'rafael_lucen@hotmail.com '


log = open(r"C:\Users\USER\Desktop\dados_rafa\login.txt", "r")
login = log.read()
senha = login

    #currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse. currentMouseX, currentMouseY (1314, 345)
def inicia_live():
    
    sleep(3)
    
    chrome = 'automaçao_cordenada\chrome.png'
    pyautogui.click(chrome)
    sleep(3)
        
    sleep(2)
    
    print('error2')
    sleep(3)
    pyautogui.click(600, 600)
    sleep(3)
    print('error1')
    pyautogui.write('https://www.youtube.com/')
    pyautogui.press(['Enter'])
    sleep(3)
    pyautogui.click('./abrir_tela.png')
    #pyautogui.locateOnScreen('looksLikeThis.png')  # returns (left, top, width, height) of first place it is found (863, 417, 70, 13)
    #pyautogui.hotkey('ctrl', 'c')  # ctrl-c to copy
    #for i in pyautogui.locateAllOnScreen('looksLikeThis.png')
    #pyautogui.position()(187, 567)
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