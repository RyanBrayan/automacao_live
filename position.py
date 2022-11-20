from time import sleep
import pyautogui
from datetime import datetime
import os


sleep(3)
# pyautogui.press('win')
# pyautogui.write('whatsa')
# sleep(0.5)
# pyautogui.press('enter')
# os.startfile(r'C:\Users\Admin\AppData\Local\WhatsApp')#clica no whatsapp

# pyautogui.click(x=618, y=362, clicks=2)
# sleep(1)
# pyautogui.press('backspace')
# pyautogui.press('backspace')#apaga ela
# pyautogui.write(datetime.today().strftime('%m'))#Inserir data atual
# sleep(1)
# pyautogui.click(x=558, y=359)#Vai realizar mesmo processo que a parte de cima
# sleep(1)
# pyautogui.press('backspace')
# pyautogui.press('backspace')
# sleep(1)
# pyautogui.write(datetime.today().strftime('%d'))
print(pyautogui.position())
# pyautogui.write('açãão')

from datetime import datetime



data_atual = datetime.today().strftime('%A')
print(type(data_atual))