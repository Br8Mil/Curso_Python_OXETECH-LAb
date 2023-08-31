resposta = 'S'
soma = 0
while resposta != 'N':
    num = int(input('Digite um número: '))
    resposta = str(input('Você quer continuar? [S/N]: ')).upper()[0]
    soma = soma + num
print(f'\nA soma deu {soma}.\n\nOk, Finalizamos o programa por aqui.')
