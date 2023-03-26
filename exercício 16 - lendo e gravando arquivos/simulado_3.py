# python simulado_3.py ex16_texto.txt
from sys import argv

script, filename = argv

print('Nós vamos esvaziar o arquivo {}'.format(filename))
print('Se não quer fazer isso, aperte CTRL-C')
print('Se quer fazer isso, aperte enter')

input('sua decisão?: ')

print('abrindo o arquivo...')
arquivo_alvo = open(filename, 'w')

print('Esvazinado o arquivo. adeus')
arquivo_alvo.truncate

print('Vou pedir para você digitar 3 linhas: ')

linha1 = input('Linha 1: ')
linha2 = input('Linha 2: ')
linha3 = input('Linha 3: ')

arquivo_alvo.write({}, {}, {}.format(linha1, linha2, linha3))

print('Vou mostrar o arquivo que você alterou')
print(arquivo_alvo.read())

print('salvando e fechando...')
arquivo_alvo.close