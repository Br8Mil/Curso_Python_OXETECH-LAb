import time

a = float(input('Quantos reais você possui?\n\nDigite o valor separando com.: '))
pergunta = input(f'''\nBem você nos disse que tem R${a}, quer saber quanto terá em dolar?

Sim ou Não? ''')
resposta = pergunta.lower()

if resposta == 'sim':
    pass
else:
    print('\nBom quando quiser inice o programa novamente')
    time.sleep(7)
    exit()
cotacao = 4.96
valor = a / cotacao
print(f'\nvocê possui ${valor:,.2f} da terra do tio Sam.')