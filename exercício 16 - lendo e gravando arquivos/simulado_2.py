# lendo o arquivo alterado no exercício
# python simulado_2.py ex16_texto.txt
from sys import argv

script, filename = argv

print('vamos abrir o arquivo que você alterou')

texto = open(filename)

print('Esse é o texto:')
print('')

print(texto.read())