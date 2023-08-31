n1 = int(input('Digite um número: '))
n2 = int(input('\nDigite outro número: '))
soma = n1 + n2
sub = n1 - n2
multi = n1 * n2
div = n1 / n2
div_inteira = n1 // n2
expo = n1 ** n2
resto = n1 % n2

print(f'''\nO primeiro número digitado foi {n1}, e o segundo foi {n2}

Sua soma e {soma}, sua subtração e {sub}, a sua multiplicação e {multi}, e sua divisão e {div:,.3f}

sua divisão inteira e {div_inteira} e sua exponenciação e {expo} e para finalizar  o seu resto e {resto}

E assim temos o resultado de todas as operações.''')