print('###Descontão###')
a = int(input('\nDigite o valor do produto: '))
desconto = a / 100 * 5
print(f'''\nSeu produto recebeu 5% de desconto e seu valor final e: R$ {a - desconto}''')