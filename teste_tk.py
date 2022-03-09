from tkinter import *
from tkinter import messagebox


def entrar():
    # Toplevel() porque já existe uma janela principal (janelaprincipal = Tk())
    janela = Toplevel()
    janela.title("Salvadados")
    janela.geometry('400x600')

    Lab1 = Label(janela, text='Nome completo:')
    Lab1.pack()
    textao = Entry(janela, textvariable=var, borderwidth=5, relief='ridge')
    textao.pack()

    Lab2 = Label(janela, text='Idade:')
    Lab2.pack()
    textao2 = Entry(janela, textvariable=d, borderwidth=5, relief='ridge')
    textao2.pack()

    Lab3 = Label(janela, text="Sexo:")
    Lab3.pack()

    # kw = StringVar()
    RBTN1 = Radiobutton(janela, text='Feminino', variable=kw, value='Feminino')
    RBTN1.pack()
    RBTN2 = Radiobutton(janela, text='Masculino', variable=kw, value='Masculino')
    RBTN2.pack()

    Lab4 = Label(janela, text="Estado:")
    Lab4.pack()

    # Botão que irá chamar a nova tela ou tkinter messagebox.
    btn_salvar = Button(janela, text='Salvar dados', command=lambda: janelanova(var, d, kw))
    btn_salvar.pack()

    btn_salvar = Button(janela, text='Salvar dados (messagebox)', command=lambda: janela_confirmacao(var, d, kw))
    btn_salvar.pack(pady=10)


def janelanova(var, d, kw):
    k = Toplevel()
    k.title("Salvadados")
    k.geometry('100x120')
    L2 = Label(k, text='Dados salvos:', bg='Red', fg='White')
    L2.pack()
    L = Label(k, text=var.get())
    L.pack()
    L3 = Label(k, text=d.get())
    L3.pack()
    L4 = Label(k, text=kw.get())
    L4.pack()


def janela_confirmacao(var, d, kw):
    msg = f'Ceia'
    resposta = messagebox.askokcancel(title='Confirmar?', message=msg)
    print(resposta)
    if resposta is True:
        print('Você clicou em OK')
    else:
        print('Você clicou em CANCELAR ou fechou a janela')


def sair():
    janelaprincipal.quit()


# JanPrincipal
janelaprincipal = Tk()
janelaprincipal.title('Menu Principal')
janelaprincipal.geometry('1010x200')
janelaprincipal['bg'] = '#C1FFC1'

mensagem1 = Label(janelaprincipal,
                  text='Seja bem-vindo à Programação de Eventos do IFSP -Câmpus Jacareí,'
                       'cadastre-se para visualizar os eventos e suas programações completas.',
                  font=' -size 12', bg='green', fg='white')
mensagem1.place(x=1, y=14)

botaocadastro = Button(janelaprincipal, text='Cadastrar', font='-weight bold -size 16',
                       bg='green', fg='white', width=20, activebackground='#B4EEB4', command=entrar)
botaocadastro.place(x=355, y=60)

botaosair = Button(janelaprincipal, text='Sair', font='-weight bold -size 16',
                   bg='green', fg='white', width=20, activebackground='#B4EEB4', command=sair)
botaosair.place(x=355, y=120)

# Variáveis
var = StringVar()
d = StringVar()
var2 = StringVar()
kw = StringVar()

mainloop()