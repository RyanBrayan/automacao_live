from time import sleep
import pyautogui
from datetime import datetime


def canvasDowload():
    pyautogui.click(x=1593, y=125)#compartilhar
    sleep(2)
    pyautogui.click(x=1485, y=607)#Baixar
    sleep(2)
    pyautogui.click(x=1635, y=504)#abre folhas
    sleep(2)
    pyautogui.click(x=1616, y=561)#seleciona todas as páginas
    sleep(2)
    pyautogui.click(x=1615, y=617)#Seleciona folha atual
    sleep(2 )
    pyautogui.click(x=1502, y=808)#Pronto
    sleep(2)
    pyautogui.click(x=1463, y=618)#Baixa a imagem