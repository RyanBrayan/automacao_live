from time import sleep
from tkinter import *
from tkinter import messagebox
from automacao_face_live import inicia_live, capa

janela = Tk()

janela.title('Que culto é hoje ? :)')
janela.geometry('300x300+420+300')

def botoes_tipo_culto():
    btn_salvar_ceia = Button(janela, text='Culto de Ceia', bg= 'white', activebackground= 'gray', font="Helvetica", command=lambda:janela_confirmacao_ceia(var, d, kw))
    btn_salvar_ceia.pack(pady=25, side= TOP)

    btn_salvar_normal = Button(janela, text='Culto normal', bg= 'white', activebackground= 'gray', font="Helvetica", command=lambda: janela_confirmacao_normal(var, d, kw))
    btn_salvar_normal.pack(pady=25, side= TOP)

    btn_salva_jovens = Button(janela, text='Culto de Jovens', bg= 'white', activebackground= 'gray', font="Helvetica", command=lambda: janela_confirmacao_jovens(var, d, kw))
    btn_salva_jovens.pack(pady=25, side= TOP)


def janela_confirmacao_ceia(var, d, kw):
    msg = f'Voce apertou em Culto Ceia'
    resposta_ceia = messagebox.askokcancel(title='Confirmar ?', message=msg)
    #Vai executar as porrada de elemento 
    if resposta_ceia is True:
        print('')
        inicia_live()

        janela.destroy()
        
def janela_confirmacao_normal(var, d, kw):
    msg = f'Voce apertou em Culto Normal'
    resposta_normal = messagebox.askokcancel(title='Confirmar ?', message=msg)
    if resposta_normal is True:
        janela.destroy()
        inicia_live()
        capa()
        


def janela_confirmacao_jovens(var, d, kw):
    msg = f'Voce apertou em Culto Jovens'
    resposta_jovens = messagebox.askokcancel(title='Confirmar ?', message=msg)
    if resposta_jovens is True:
        janela.destroy()
        
     
        
var = StringVar()
d = StringVar()
var2 = StringVar()
kw = StringVar()

botoes_tipo_culto()
janela.mainloop()

