# python ex16.py ex16_texto.txt
from sys import argv

script, filename = argv

print(f'we agre going to erase {filename}')
print(' if you dont want that, hit CRTL-C(^C).')
print('if you do want that, hit RETURN')

input('?')

print('opening the file...')
target = open(filename, 'w')

print('truncating the file. goodbye')
target.truncate # esvazia o arquivo

print('now i am going to ask you for three lines')

line1 = input('line 1: ')
line2 = input('line 2: ')
line3 = input('line 3: ')

print('i am going to write these to the file')

target.write(line1) # escreve coisas no arquivo
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print('and finally, we close it')
target.close() # fecha e salva o arquivo