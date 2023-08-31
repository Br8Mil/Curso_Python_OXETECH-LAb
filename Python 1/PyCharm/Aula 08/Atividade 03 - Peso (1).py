pesso_maior = 0
pesso_menor = 1000
for c in range(1, 6):
    num = int(input(f'Digite o peso da {c}° pessoa: '))
    if num >= pesso_maior:
        pesso_maior = num
    elif num <= pesso_menor:
        pesso_menor = num

print(f'\nA pessoa que pesa mais: {pesso_maior}Kg.\nA pessoa que tem o pesso menor: {pesso_menor}Kg.')