import random

print('##O Professor Pajé quer sortear a ordem de apresentação de 4 alunos.\nDesenvolva um algoritimo para me ajudar.###\n')

a = input('Digite o nome da primeiro aluno: ')
b = input('\nDigite o nome da segundo aluno: ')
c = input('\nDigite o nome da terceiro aluno: ')
d = input('\nDigite o nome da quarto aluno: ')

lista = [a, b, c, d]

random.shuffle(lista)

print(f'\n{lista}')