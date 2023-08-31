preco = float(input('Digite o valor do produto: '))

p1 = (10/100) * preco
p2 = (5/100) * preco
p3 = preco / 2
p4 = (10/100) * preco
p5 = preco + p4

print('''\nQual e a condição de pagamento?

[1] - Dinheiro ou cheque.
[2] - Cartão.
[3] - 2x no cartão.
[4] - 3x ou mais no cartão.''')

pagamento = int(input('\ne ai qual você escolhe? \n'))

if pagamento == 1:
    print(f'O Desconto será de R$ {p1}, e o valor final da compra é R$ {preco - p1}.')
elif pagamento == 2:
    print(f'O Desconto será de R$ {p2}, e o valor final da compra é R$ {preco - p2}.')
elif pagamento == 3:
    print(f'O Desconto será dividido em duas parcelas de R$ {p3} cada, sem juros.')
else:
    print(f'O Desconto será dividido em três parcelas de R$ {p5 / 3:,.2f} cada, adicionado 10 % de juros.\nO valor final será de {preco + p4}.')