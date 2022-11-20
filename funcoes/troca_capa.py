from time import sleep
import pyautogui
from datetime import datetime
import os
from types import NoneType


meses = {
    'January' : 'jan',
    'February' : 'fev',
    'March' : 'mar',
    'April' : 'abr', 
    'May' : 'maio',
    'June' : 'junho', 
    'July' : 'julho',
    'August' : 'agosto',
    'September' : 'setembro',
    'October' : 'outubro',
    'November' : 'novembro',
    'December' : 'dezembro'
        
}



def troca_capa(data_atual):
    sleep(18)
    pyautogui.hotkey('ctrl', 'w')
    sleep(2)
    pyautogui.click(x=1209, y=582)
    pyautogui.hscroll(-300)   # desce 300 pexels com a barra pra trocar a capa
    sleep(2)
    pyautogui.moveTo(x=604, y=655)
    sleep(1)
    pyautogui.click(x=604, y=655) 
    sleep(2)
    pyautogui.click(x=544, y=658)
    sleep(2)
    pyautogui.click(x=223, y=189, clicks=2)#seleciona capa
    sleep(2)
    pyautogui.click(x=1203, y=876)
    sleep(2)
    pyautogui.click(x=1203, y=876)
    sleep(2)
    pyautogui.click(x=1191, y=511)#CLICA PRA DESCER
    sleep(0.5)
    pyautogui.scroll(-300)
    sleep(1)
    pyautogui.click(x=638, y=783)#ABRE AGENDA 

    data = meses[datetime.today().strftime('%B')] 
    pyautogui.hotkey('ctrl', 'a')

    sleep(0.5)
    pyautogui.write(datetime.today().strftime(f'%d de {data}. de %Y'))# ex: 6 de mar. de 2022
    sleep(0.5)
    pyautogui.click(x=740, y=781)
    sleep(0.5)
    pyautogui.click(x=740, y=781)
    pyautogui.hotkey('ctrl', 'a')
    
    if data_atual == 'Sunday':
        pyautogui.write('17:45')#HORA
    else:
        pyautogui.write('19:45')

    sleep(1)
    pyautogui.click(x=498, y=627, clicks=2, interval=1)#muda pa publico
    sleep(1)
    pyautogui.click(x=1221, y=883, clicks=2)#inicia live
    sleep(10)
    
    pyautogui.click(x=1637, y=130)#aperta no icon perfil
    sleep(1)
    pyautogui.click(x=1515, y=247)
    sleep(7)
    pyautogui.click(x=1494, y=446)

    sleep(8)
    pyautogui.click(x=404, y=261)
    sleep(10)
    pyautogui.click(x=621, y=476)
    sleep(1)
    pyautogui.click(x=499, y=503)#copia o link
    sleep(2)
    
    # os.startfile(r'C:\Users\Admin\AppData\Local\WhatsApp\Update.exe')#clica no whatsapp

    pyautogui.press('win')
    pyautogui.write('whatsa')
    sleep(0.5)
    pyautogui.press('enter')
    while True:
        img = pyautogui.locateOnScreen(r'img\lupa.png')#Procura pela lupa de pesquisa
        if type(img) != NoneType:
            pyautogui.click(r'img\lupa.png')#Procura pela lupa de pesquisa
            break
    sleep(1)
    pyautogui.write('I.B.B. Oficial' , 0.1)
    sleep(1)
    pyautogui.click(x=265, y=214)
    sleep(1)
    
    #faltando parte de manda link 
    if data_atual == 'Wednesday': 
        pyautogui.write('A paz meus irmãos! 🙌🙏 Esse é o link do culto de hoje, a partir das 20h10: ')
        sleep(1)
        pyautogui.hotkey('ctrl', 'v')
        sleep(4)
        # pyautogui.keyDown('ENTER') 
    else:
        pyautogui.write('A paz meus irmãos! 🙌🙏 Esse é o link do culto de hoje, a partir das 18h: ')
        sleep(1)
        pyautogui.hotkey('ctrl', 'v')
        sleep(4)
        # pyautogui.keyDown('ENTER')