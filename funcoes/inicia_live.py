from time import sleep
import pyautogui
import os



def inicia_live(culto, data_atual):
    pyautogui.alert('Automação iniciada apenas aperte em "OK" e NÃO MECHA mais no Mouse ou Teclado')
    sleep(3)
    os.startfile(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
    sleep(3)
    pyautogui.click(x=577, y=50) #youtu04
    sleep(3)
    pyautogui.write("https://www.youtube.com/channel/UCDCBGGUtwOt4wJ8nFAHnP-A", 0.1)#logo-ibb
    pyautogui.hotkey('Enter')
    # pyautogui.click(x=1516, y=330)#youtube-studio
    sleep(10)
    pyautogui.click(x=1507, y=129)#botao-live
    sleep(5)
    pyautogui.click(x=1430, y=212)#entrar pra agendar
    sleep(10)
    pyautogui.click(x=31, y=290)#clica no botão de Gerenciar
    sleep(4)
    pyautogui.click(x=1525, y=196)#agendar
    sleep(4)
    pyautogui.click(x=1550, y=245)#Software de codificação
    sleep(10)
    pyautogui.click(x=1062, y=575)#clica live
    sleep(3)
    pyautogui.click(x=805, y=676)#troca a live
    sleep(3)
    pyautogui.click(x=1048, y=695)#reutiliza a live
    sleep(3)
    pyautogui.click(x=726, y=595)#aperta na descrição
    pyautogui.hotkey('ctrl', 'a') #seleciona descrição
    sleep(3)

    if data_atual == 'Wednesday': #verifica que dia é hoje 
        pyautogui.write(f'I.B.B. Culto {culto} | (Live Youtube/Facebook) - Igreja Batista Bereana em Franco da Rocha') #escreve na descrição
        pyautogui.click(x=920, y=427)#aperta no titulo da live
        pyautogui.hotkey('ctrl', 'a')#seleciona ele
        sleep(2)
        pyautogui.typewrite(f'I.B.B. Culto {culto} | (Live Youtube/Facebook) a partir das 20h10')
    #Lembrar de verificar se é domingo ou sabado 
    elif data_atual == 'Saturday':
        pyautogui.write(f'I.B.B. {culto} | (Live Youtube/Facebook) - Igreja Batista Bereana em Franco da Rocha') #escreve na descrição
        pyautogui.click(x=920, y=427)#aperta no titulo da live
        pyautogui.hotkey('ctrl', 'a')#seleciona ele
        sleep(2)
        pyautogui.write(f'I.B.B. {culto} | (Live Youtube/Facebook) a partir das 18h')
    else:
        pyautogui.write(f'I.B.B. {culto} | (Live Youtube/Facebook) - Igreja Batista Bereana em Franco da Rocha') #escreve na descrição
        pyautogui.click(x=920, y=427)#aperta no titulo da live
        pyautogui.hotkey('ctrl', 'a')#seleciona ele
        sleep(2)
        pyautogui.write(f'I.B.B. {culto} | (Live Youtube/Facebook) a partir das 18h')

    pyautogui.hotkey('ctrl', 't')#nova pagina
    sleep(1)
    pyautogui.click(x=720, y=83)#aperta no canvas
    sleep(10)