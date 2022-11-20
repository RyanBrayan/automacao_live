from time import sleep
import pyautogui
from datetime import datetime
from funcoes import canvasDowload

def capa_culto_normal(data_atual):
    #if data_atual == 'Wednesday': #verifica novamente que dia é hoje pra ver a capa certa
    sleep(3)
    if data_atual == 'Wednesday':
        sleep(2)
        pyautogui.click(x=458, y=385)
        pyautogui.hscroll(700)
        sleep(0.5)
        pyautogui.click(x=652, y=341, clicks=2)
        sleep(1)
        pyautogui.press('backspace')
        pyautogui.press('backspace')#apaga ela
        pyautogui.write(datetime.today().strftime('%m'))#Inserir data atual
        sleep(1)
        pyautogui.click(x=578, y=333)#Vai clicar na data
        sleep(0.5)
        pyautogui.press('backspace')
        pyautogui.press('backspace')#apaga ela
        pyautogui.write(datetime.today().strftime('%d'))#Inserir data atual
        sleep(1)
        canvasDowload.canvasDowload()
        

    else:
        pyautogui.click(x=458, y=385)
        pyautogui.hscroll(700)
        sleep(0.5)
        pyautogui.hscroll(-750)#Vai descer ate a page de domingo
        sleep(1)
        pyautogui.click(x=634, y=401, clicks=2)
        sleep(1)
        pyautogui.press('backspace')
        pyautogui.press('backspace')#apaga ela
        pyautogui.write(datetime.today().strftime('%m'))#Inserir data atual
        sleep(1)
        pyautogui.click(x=567, y=403)#Vai realizar mesmo processo que a parte de cima
        sleep(1)
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        sleep(1)
        pyautogui.write(datetime.today().strftime('%d'))
        sleep(1)
        canvasDowload.canvasDowload()
