from time import sleep
import pyautogui
from types import NoneType




def troca_canal():
    sleep(2)
    pyautogui.hotkey('alt', 'f4')
    sleep(2)
    pyautogui.click(x=1617, y=126)#logo-ibb
    sleep(2)
    pyautogui.click(x=1534, y=327)#aperta PARA trocar de conta
    sleep(2)
    pyautogui.click(x=1475, y=445)#aperta na conta
    sleep(10)
    pyautogui.click(x=1548, y=132)
    sleep(2)
    pyautogui.click(x=1501, y=201)#ja esta na parte de trasmissão
    sleep(10)
    pyautogui.click(x=587, y=726)#copia url de stream
    sleep(1)
    pyautogui.hotkey('windows', 'r')
    pyautogui.hotkey('enter')
    pyautogui.write(r'C:\Users\Admin\Downloads\obs-studio\bin\64bit\" obs64.exe')
    pyautogui.hotkey('enter')
    while True:
        img = pyautogui.locateOnScreen(r'img\x.png')#Fecha erros
        if type(img) != NoneType:
            pyautogui.click(r'img\x.png')#Fecha erros
            break
    sleep(1)
    # pyautogui.moveTo(1613, 124)
    # sleep(2)
    # pyautogui.drag(-600, 0, 2, button='left')#arrasta o layout do youtube e facebook
    # sleep(1)
    # pyautogui.moveTo(1423, 258)
    # sleep(1)
    # pyautogui.drag(0, 60, 2, button='left')
    # sleep(1)
    # pyautogui.click(1353, 173)#clica modifica yoube
    # sleep(2)
    # pyautogui.click(x=858, y=410)#clica url de stream
    # sleep(1)
    # pyautogui.hotkey('ctrl', 'a')
    # pyautogui.hotkey('ctrl', 'v')
    # sleep(1)
    # pyautogui.hotkey('alt', 'tab')#volta pro youtube
    # sleep(1)
    # pyautogui.click(x=591, y=670)#copia chave
    # sleep(1)
    # pyautogui.hotkey('alt', 'tab')
    # sleep(1)
    # pyautogui.click(827, 440)#clica pra mudar chave
    # sleep(0.5)
    # pyautogui.hotkey('ctrl', 'a')
    # pyautogui.hotkey('ctrl', 'v')
    # sleep(0.5)
    pyautogui.click(x=1473, y=869)
    sleep(1)
    pyautogui.click(x=434, y=201)
    sleep(1)
    pyautogui.click(x=984, y=229)
    sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'v')
    sleep(1)
    pyautogui.click(x=1270, y=847)
    sleep(1)
    pyautogui.click(x=1110, y=848)
    sleep(1)
    pyautogui.click(x=1443, y=752)#inicia transmissão
    sleep(1)
    pyautogui.click(x=1447, y=780)
    sleep(2)
    pyautogui.click(x=871, y=536)
    sleep(2)
    pyautogui.click(x=1056, y=549)#clica em ok
    sleep(0.5)
    pyautogui.click(x=1119, y=173)#inicia live
    pyautogui.hotkey('alt', 'tab')
    sleep(9)
    pyautogui.hotkey('alt', 'tab')
    sleep(1)
    pyautogui.click(x=70, y=858)
    sleep(1)
    pyautogui.click(x=403, y=892, clicks=2)#abre a camera pra editar
    sleep(2)
    pyautogui.click(x=679, y=623)
    sleep(2)
    pyautogui.click('img\padrao.png')
    sleep(1)
    pyautogui.click('img\controle_camera.png')#abre para editar o foco 
    sleep(1)
    pyautogui.click('img\padrao.png')
    sleep(1)
    pyautogui.click('img\certin.png')#desfrega p certin do foco
    sleep(0.5)
    pyautogui.move(-213, 0)#0 zera o foco
    sleep(0.5)
    pyautogui.drag(-35, 0, 2, button='left')
    sleep(1)
    pyautogui.click('img\certin.png')
    sleep(0.5)
    pyautogui.click('img\aplicar.png')#aplica as config
    sleep(0.5)
    pyautogui.move(-170, 0 )#ok
    pyautogui.click(0, 0)#POSSIVEL ERROOOO AQUI
    sleep(1)
    pyautogui.click(x=1073, y=786)
    sleep(1)
    

    #pyautogui.locateOnScreen('looksLikeThis.png')  # returns (left, top, width, height) of first place it is found (863, 417, 70, 13)
    #pyautogui.hotkey('ctrl', 'c')  # ctrl-c to copy
    #for i in pyautogui.locateAllOnScreen('looksLikeThis.png')
    #pyautogui.position()(187, 567)
    #write para escrever os codigos