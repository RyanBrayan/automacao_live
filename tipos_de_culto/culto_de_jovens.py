from time import sleep
import pyautogui
from datetime import datetime
from funcoes import canvasDowload



def capa_jovens(buscaData):
    sleep(2)
    pyautogui.click(x=458, y=385)
    pyautogui.hscroll(700)
    sleep(0.5)

    pyautogui.hscroll(-2450)#Vai descer ate a page de domingo

    sleep(1)
    pyautogui.click(x=609, y=357, clicks=2)
    sleep(1)
    pyautogui.press('backspace')
    pyautogui.press('backspace')#apaga ela
    pyautogui.write(datetime.today().strftime('%m'))#Inserir data atual
    sleep(1)
    pyautogui.click(x=550, y=356)#Vai realizar mesmo processo que a parte de cima
    sleep(1)
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    sleep(1)
    pyautogui.write(datetime.today().strftime('%d'))
    sleep(1)
    canvasDowload.canvasDowload()
