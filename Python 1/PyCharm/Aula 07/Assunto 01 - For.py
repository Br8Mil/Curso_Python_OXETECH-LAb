#inicio = int(input('Começa a contagem de que número? '))
#fim = int(input('vai até? ')) + 1
#passo = int(input('vai de 1 em 1 ou pulando? (digite o número): '))
#for c in range(inicio, fim, passo):
    #print(f'{c}º contagem')

soma = 0
for c in range(1, 6):
    num = int(input(f'Digite o {c} número: '))
    soma = soma + num
print(f'O resultado foi {soma}.')