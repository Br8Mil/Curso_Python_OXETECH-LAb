np = 0
ni = 0
soma = 0
texto = 1

while texto != 7:
    pergunta = int(input(f'Digite o número {texto}: '))
    if pergunta % 2 == 0:
        soma = soma + pergunta
        np = np + 1
        texto = texto + 1
    else:
         ni = ni + 1
         texto = texto + 1

print(f'\nvocê digitou {np} números pares, e digitou {ni} números ímpares, sendo assim a soma total dos números pares é: {soma}')