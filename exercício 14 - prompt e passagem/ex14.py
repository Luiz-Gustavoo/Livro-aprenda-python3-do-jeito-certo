# python ex14.py luiz
from sys import argv

script, user_name, user_age = argv

prompt = ('your answser: ')

print(f'hi {user_name},  i"m the {script} script.')
print(f'your age is {user_age}')

print(f'do you like me {user_name}?')
likes = input(prompt)

print(f'what kind of computer do you have {user_name}?')
computer = input(prompt)
