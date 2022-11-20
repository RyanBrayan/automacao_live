# -*- coding: UTF-8 -*-
from time import sleep
from types import NoneType
import pyautogui
from datetime import datetime
from time import sleep
from tkinter import *
from tkinter import messagebox
import buscaData
import os
from tipos_de_culto import culto_ceia, culto_de_jovens, culto_normal
from funcoes import inicia_live, troca_capa, troca_canal

data_atual = buscaData.dataAtualWeb()


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


janela = Tk()
janela.title('Que culto é hoje ? :)')
janela.geometry('300x300+420+300')

def botoes_tipo_culto():
    btn_salvar_ceia = Button(janela, text='Culto de ceia', bg= 'white', activebackground= 'gray', font="Helvetica", command=lambda:janela_confirmacao_ceia(var, d, kw))
    btn_salvar_ceia.pack(pady=25, side= TOP)

    btn_salvar_normal = Button(janela, text='Culto normal', bg= 'white', activebackground= 'gray', font="Helvetica", command=lambda: janela_confirmacao_normal(var, d, kw))
    btn_salvar_normal.pack(pady=25, side= TOP)

    btn_salva_jovens = Button(janela, text='Culto de jovens', bg= 'white', activebackground= 'gray', font="Helvetica", command=lambda: janela_confirmacao_jovens(var, d, kw))
    btn_salva_jovens.pack(pady=25, side= TOP)


def janela_confirmacao_ceia(var, d, kw):
    msg = f'Voce apertou em culto de CEIA, confirma?'
    resposta_ceia = messagebox.askokcancel(title='Confirmação', message=msg)
    #Vai executar as porrada de elemento 
    if resposta_ceia is True:
        janela.destroy()
        inicia_live.inicia_live('Culto de Ceia', data_atual)
        culto_ceia.capa_ceia(data_atual)
        troca_capa.troca_capa(data_atual)
        troca_canal.troca_canal()  


def janela_confirmacao_normal(var, d, kw):
    msg = f'Voce apertou em culto NORMAL, confirma?'
    resposta_normal = messagebox.askokcancel(title='Confirmação', message=msg)
    if resposta_normal is True:
        janela.destroy()
        if data_atual == 'Saturdayd':
            inicia_live.inicia_live('Culto de Sábado', data_atual)
        else:
            inicia_live.inicia_live('Culto de Domingo', data_atual)

        culto_normal.capa_culto_normal(data_atual)
        troca_capa.troca_capa(data_atual)
        troca_canal.troca_canal()


def janela_confirmacao_jovens(var, d, kw):
    msg = f'Voce apertou em culto dos JOVENS, confirma?'
    resposta_jovens = messagebox.askokcancel(title='Confirmação', message=msg)
    if resposta_jovens is True:
        janela.destroy()
        inicia_live.inicia_live('Culto dos Jovens', data_atual)
        culto_de_jovens.capa_jovens(data_atual)
        troca_capa.troca_capa(data_atual)
        troca_canal.troca_canal()



var = StringVar()
d = StringVar()
var2 = StringVar()
kw = StringVar()

    
#OK
        


if data_atual == 'Wednesday':
    inicia_live.inicia_live('Quarta-feira', data_atual)
    culto_normal.capa_culto_normal(data_atual)
    troca_capa.troca_capa(data_atual) 
    troca_canal.troca_canal() 
else:
    botoes_tipo_culto()
    janela.mainloop()
 