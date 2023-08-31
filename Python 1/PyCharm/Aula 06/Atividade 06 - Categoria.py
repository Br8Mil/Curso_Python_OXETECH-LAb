from datetime import date
ano = date.today().year

nascimento = int(input('Digite o ano do seu nascimento: '))
idade_2 = ano - nascimento
print(f'Sua idade é {idade_2}.')

if idade_2 <= 9:
    print('Você e da categoria mirim.')
elif idade_2 <= 14:
    print('Você e da categoria infantil.')
elif idade_2 <= 17:
    print('Você e da categoria junior.')
elif idade_2 <= 20:
    print('Você e da categoria sênior.')
else:
    print('Você e da categoria master.')

