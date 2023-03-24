# python ex15_2.py
arquiv_input = input('digite o nome do arquivo: ')

txt = open(arquiv_input) # objeto file: o arquivo fica salvo aqui
print(f'nome do arquivo: {arquiv_input}')
print(txt.read()) # ler o objeto file atribuido a txt