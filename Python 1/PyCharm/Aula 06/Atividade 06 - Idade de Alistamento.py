from datetime import date
ano = date.today().year

nascimento = int(input('Digite o ano em que você nasceu: '))
print()

idade = ano - nascimento

falta = 18 - idade

passou = idade - 22

print(f'Você tem {idade} anos.')

if idade >= 23:
    print(f'Você já supera a idade máxima de 22 anos, passando-a em {passou} anos.')
elif idade >= 18:
    print('Você está em idade de se alistar.')
else:
    print(f'Você não possui a idade minima de 18 anos para o alistamento.\nAinda faltam {falta} anos.')