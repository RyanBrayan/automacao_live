from tabula import read_pdf
import pandas as pd

arquivo = open('paes.txt', 'w')
lendo = arquivo.readline()
for c in arquivo:
    print(c)