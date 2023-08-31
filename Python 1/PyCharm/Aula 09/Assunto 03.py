np = 0
ni = 0
num = 1
while num != 0:
    num = int(input('Digite um número: \nou zero para parar:  '))
    if num != 0:
        if num % 2 == 0:
            np = np + 1
        else:
            ni = ni + 1
print(f'\nO número de pares foi {np}.\nE de ímpares foi {ni}.')