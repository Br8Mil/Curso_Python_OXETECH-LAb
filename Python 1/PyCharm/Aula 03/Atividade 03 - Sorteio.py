import random

print('##O Professor Pajé quer sortear entre 4 alunos, qual irá apagar o quadro###\n')

a = input('Digite o nome da primeira vitima: ')
b = input('\nDigite o nome da segunda vitima: ')
c = input('\nDigite o nome da terceira vitima: ')
d = input('\nDigite o nome da quarta vitima: ')

lista = [a, b, c, d]

print(f'\nO sortudo/a foi {random.choice(lista)}.')
