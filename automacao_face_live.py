# -*- coding: UTF-8 -*-
from time import sleep
from types import NoneType
import pyautogui
from datetime import datetime
import culto_tk

data_atual = datetime.today().strftime('%A')


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

if data_atual == 'Wednesday':
    print('')
else:
    culto_tk.botoes_tipo_culto()
    #currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse. currentMouseX, currentMouseY (1314, 345)
def inicia_live():
    print('\033[1;41m  VOCÊ INICIOU A AUTOMAÇÃO NÃO MECHA NO MOUSE OU TECLADO  \033[m')
    sleep(3)
    pyautogui.click(x=269, y=1032)
    sleep(3)
    pyautogui.click(x=265, y=74) #youtube
    sleep(9)
    pyautogui.click(x=1617, y=126)#logo-ibb
    sleep(1)
    pyautogui.click(x=1516, y=330)#youtube-studio
    sleep(10)
    pyautogui.click(x=1564, y=132)#botao-live
    sleep(2)
    pyautogui.click(x=1536, y=207)#entrar pra agendar
    sleep(7)
    pyautogui.click(x=30, y=296)
    sleep(4)
    pyautogui.click(x=1525, y=196)#agendar
    sleep(1)
    pyautogui.click(x=1062, y=575)#clica live
    sleep(1)
    pyautogui.click(x=805, y=676)#troca a live
    sleep(1)
    pyautogui.click(x=1033, y=676)#reutiliza a live
    sleep(3)
    pyautogui.click(x=726, y=595)#aperta na descrição
    pyautogui.hotkey('ctrl', 'a') #seleciona descrição
    sleep(1)

    if data_atual == 'Wednesday': #verifica que dia é hoje 
        pyautogui.write('I.B.B. Culto Quarta-feira | (Live Youtube/Facebook) - Igreja Batista Bereana em Franco da Rocha') #escreve na descrição
        pyautogui.click(x=920, y=427)#aperta no titulo da live
        pyautogui.hotkey('ctrl', 'a')#seleciona ele
        sleep(2)
        pyautogui.typewrite('I.B.B. Culto Quarta-feira | (Live Youtube/Facebook)  as 20h')
    #Lembrar de verificar se é domingo ou sabado 
    else:
        pyautogui.write('I.B.B. Culto Domingo | (Live Youtube/Facebook) - Igreja Batista Bereana em Franco da Rocha') #escreve na descrição
        pyautogui.click(x=920, y=427)#aperta no titulo da live
        pyautogui.hotkey('ctrl', 'a')#seleciona ele
        sleep(2)
        pyautogui.write('I.B.B. Culto Domingo | (Live Youtube/Facebook)  as 18h')
    
    pyautogui.hscroll(-300)   # desce 300 pexels com a barra pra trocar a capa
    sleep(1)
    pyautogui.hotkey('ctrl', 't')#nova pagina
    sleep(1)
    pyautogui.click(x=735, y=83)#aperta no canvas
    sleep(10)
    

def capa():
    #if data_atual == 'Wednesday': #verifica novamente que dia é hoje pra ver a capa certa
    sleep(3)
    if data_atual == 'Wednesday':
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
        pyautogui.click(x=1593, y=125) #compartilhar
        sleep(2)
        pyautogui.click(x=1485, y=607)#Baixar
        sleep(2)
        pyautogui.click(x=1634, y=343)#abre folhas
        sleep(2)
        pyautogui.click(x=1615, y=456)#seleciona folha 
        sleep(2)
        pyautogui.click(x=1499, y=657)#Pronto
        sleep(2)
        pyautogui.click(x=1635, y=265)
        sleep(2)
        pyautogui.click(x=1453, y=123)
        sleep(2)
        pyautogui.click(x=1463, y=703)#Baixa a imagem

    else:
        pyautogui.click(x=458, y=385)
        pyautogui.hscroll(-1500)#Vai descer ate a page de domingo
        sleep(1)
        pyautogui.click(x=653, y=382, clicks=2)
        sleep(1)
        pyautogui.press('backspace')
        pyautogui.press('backspace')#apaga ela
        pyautogui.write(datetime.today().strftime('%m'))#Inserir data atual
        sleep(1)
        pyautogui.click(x=580, y=381)#Vai realizar mesmo processo que a parte de cima
        sleep(1)
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        sleep(1)
        pyautogui.write(datetime.today().strftime('%d'))
        sleep(1)
        pyautogui.click(x=1593, y=125) #compartilhar
        sleep(2)
        pyautogui.click(x=1485, y=607)#Baixar
        sleep(2)
        pyautogui.click(x=1634, y=343)#abre folhas
        sleep(2)
        pyautogui.click(x=1617, y=574)#seleciona folha 
        sleep(2)
        pyautogui.click(x=1499, y=657)#Pronto
        sleep(2)
        pyautogui.click(x=1635, y=265)
        sleep(2)
        pyautogui.click(x=1453, y=123)
        sleep(2)
        pyautogui.click(x=1463, y=703)#Baixa a imagem

    sleep(12)
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
    pyautogui.click(x=1204, y=853)
    sleep(2)
    pyautogui.click(x=1204, y=853)
    sleep(2)
    pyautogui.click(x=638, y=783)

    data = meses[datetime.today().strftime('%B')] 
    pyautogui.hotkey('ctrl', 'a')

    sleep(0.5)
    pyautogui.write(datetime.today().strftime(f'%d de {data}. de %Y'))# ex: 6 de mar. de 2022
    sleep(0.5)
    pyautogui.click(x=740, y=781)
    sleep(0.5)
    pyautogui.click(x=740, y=781)
    pyautogui.hotkey('ctrl', 'a')
    
    if data_atual == 'sunday':
        pyautogui.write('17:45')#HORA
    else:
        pyautogui.write('19:45')

    sleep(1)
    pyautogui.click(x=498, y=627, clicks=2, interval=1)#muda pa publico
    sleep(1)
    pyautogui.click(x=1223, y=849, clicks=2)#inicia live
    sleep(10)
    pyautogui.click(x=1637, y=130)#aperta no icon perfil
    sleep(1)
    pyautogui.click(x=1515, y=247)
    sleep(5)
    pyautogui.click(x=1494, y=446)

    sleep(7)
    pyautogui.click(x=404, y=261)
    sleep(9)
    pyautogui.click(x=629, y=451)
    sleep(1)
    pyautogui.click(x=538, y=487)#copia o link
    sleep(2)
    pyautogui.click(x=315, y=1029)#clica no whatsapp
    while True:
        img = pyautogui.locateOnScreen('lupa.png')#Fecha erros
        if type(img) != NoneType:
            pyautogui.click('lupa.png')#Fecha erros
            break
    sleep(1)
    pyautogui.write('I.B.B. Oficial' , 0.1)
    sleep(0.5)
    pyautogui.keyDown('ENTER')
    sleep(2)
    #faltando parte de manda link 
    if data_atual == 'Wednesday': 
        pyautogui.write('A paz meus irmãos! 🙌🙏 Esse é o link do culto de hoje as 20h: ')
        sleep(1)
        pyautogui.hotkey('ctrl', 'v')
        #pyautogui.keyDown('ENTER') 
    else:
        pyautogui.write('A paz meus irmãos! 🙌🙏 Esse é o link do culto de hoje as 18h: ')
        sleep(1)
        pyautogui.hotkey('ctrl', 'v')
        #pyautogui.keyDown('ENTER') 
        

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
    pyautogui.click(x=1001, y=1029)
    while True:
        img = pyautogui.locateOnScreen('x.png')#Fecha erros
        if type(img) != NoneType:
            pyautogui.click('x.png')#Fecha erros
            break
    sleep(1)
    pyautogui.moveTo(1613, 124)
    sleep(2)
    pyautogui.drag(-600, 0, 2, button='left')#arrasta o layout do youtube e facebook
    sleep(1)
    pyautogui.moveTo(1423, 258)
    sleep(1)
    pyautogui.drag(0, 60, 2, button='left')
    sleep(1)
    pyautogui.click(1353, 173)#clica modifica yoube
    sleep(2)
    pyautogui.click(x=858, y=410)#clica url de stream
    sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'v')
    sleep(1)
    pyautogui.hotkey('alt', 'tab')#volta pro youtube
    sleep(1)
    pyautogui.click(x=591, y=670)#copia chave
    sleep(1)
    pyautogui.hotkey('alt', 'tab')
    sleep(1)
    pyautogui.click(827, 440)#clica pra mudar chave
    sleep(0.5)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'v')
    sleep(0.5)
    pyautogui.click(x=839, y=648)#inicia transmissão
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
    pyautogui.click('padrao.png')
    sleep(1)
    pyautogui.click('controle_camera.png')#abre para editar o foco 
    sleep(1)
    pyautogui.click('padrao.png')
    sleep(1)
    pyautogui.click('certin.png')#desfrega p certin do foco
    sleep(0.5)
    pyautogui.move(-213, 0)#0 zera o foco
    sleep(0.5)
    pyautogui.drag(-35, 0, 2, button='left')
    sleep(1)
    pyautogui.click('certin.png')
    sleep(0.5)
    pyautogui.click('aplicar.png')#aplica as config
    sleep(0.5)
    pyautogui.move(-170, 0 )#ok
    pyautogui.click(0, 0)
    

    #pyautogui.locateOnScreen('looksLikeThis.png')  # returns (left, top, width, height) of first place it is found (863, 417, 70, 13)
    #pyautogui.hotkey('ctrl', 'c')  # ctrl-c to copy
    #for i in pyautogui.locateAllOnScreen('looksLikeThis.png')
    #pyautogui.position()(187, 567)
    #write para escrever os codigos

inicia_live()
capa()
troca_canal()  