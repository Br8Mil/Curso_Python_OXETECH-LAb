from random import randint
pesso_maior = 0
pesso_menor = 1000
for c in range(1, 6):
    num = randint(20, 300)
    print(f'O peso da {c}° pessoa é: {num}Kg.')
    if num >= pesso_maior:
        pesso_maior = num
    elif num <= pesso_menor:
        pesso_menor = num

print(f'\nA pessoa que pesa mais: {pesso_maior}Kg.\nA pessoa que tem o pesso menor: {pesso_menor}Kg.')