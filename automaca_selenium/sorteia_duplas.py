from random import shuffle
from tkinter import *
lista = [
    'Equipe_RAFAEL', 'Equipe_CAIO', 'Equipe_JOAO', 
]
shuffle(lista)


def sort_times():
    times_sorteados = []
    for nomes in range(0, 1):
        times_sorteados.append(lista[0])
        times_sorteados.append(lista[-1])
        lista.pop(0)
        lista.pop()
        print(times_sorteados)
sort_times()
