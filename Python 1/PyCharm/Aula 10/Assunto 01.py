n = 0
soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma = soma + n
print(f'A sua soma deu {soma}')
