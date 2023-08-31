totalP18 = totalM = totalM20 = 0
while True:
    idade = int(input('Digite a sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade > 18:
        totalP18 = totalP18 + 1
    if sexo == 'M':
        totalM = totalM + 1
    if sexo == 'F' and idade < 20:
        totalM20 = totalM20 + 1
    resp = ' '
    while resp not in "SN":
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'O número total de pessoas maiores de 18 foi de {totalP18}.')
print(f'O número de homens cadastrados e de {totalM}.')
print(f'O número de mulheres abaixo de 20 anos e de {totalM20}.')
