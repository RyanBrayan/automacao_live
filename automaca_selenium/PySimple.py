import PySimpleGUI as ps
from random import shuffle
lista = [
    'nome', 'nome2', 'nome3', 'nome4', 'nome5', 'nome6'
]
shuffle(lista)
print(lista)
def sort_times(num):
    for nomes in range(0, num):
        print(lista[0], lista[-1])
        lista.pop(0)
        lista.pop()
        print(lista) 
    
    
ps.theme('DarkAmber')    # Keep things interesting for your users

layout = [[ps.Text('Quantas duplas serão:')],      
          [ps.Input()],      
          [ps.Button('Enviar'), ps.Exit('Sair')]] 
window = ps.Window('Window that stays open', layout)      

while True:                             # The Event Loop
    event, values = window.read()
    for v in values:
        print(event, values)
        print(v)
        print(v.values())
        sort_times(v.values())
        print(event, values) 
    print(event, values)       
    if event == ps.WIN_CLOSED or event == 'Sair':
        break      

window.close()