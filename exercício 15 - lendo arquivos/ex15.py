# python ex15.py ex15_texto.txt
from sys import argv

script, filename = argv

txt = open(filename) # abrir o arquivo digitado

print(f'here is your file {filename}:')
print(txt.read()) # ler o arquivo digitado

print('type the filename again: ')
file_again = input('>') 

txt_again = open(file_again) # abrir o arquivo digitado
print(txt_again.read())# ler o arquivo digitado