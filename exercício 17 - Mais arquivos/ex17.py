# python ex17.py arquivo_velho.txt arquivo_novo.txt
from sys import argv
from os.path import exists

script, do_arquivo, para_arquivo = argv

print('Copiando de {} para {}'.format(do_arquivo, para_arquivo))

dentro_arquivo = open(do_arquivo) # abrindo o conteúdo de do_arquivo
lendo_arquivo = dentro_arquivo.read() # lendo o conteúdo de do_arquivo


arquivo_novo = open(para_arquivo, 'w')

arquivo_novo.write(lendo_arquivo) # gravando o conteúdo de do_arquivo(lendo_arquivo) para para_arquivo

print('Tudo feito')

dentro_arquivo.close()
arquivo_novo.close()
