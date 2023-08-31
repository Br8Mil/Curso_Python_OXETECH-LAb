salario = int(input('Digite o valor atual do salário: '))
if salario > 1500:
    print(f'\nO aumento será de R$ {(10 / 100) * salario}, sendo assim o valor final e de {salario + (10 / 100) * salario}.')
else:
    print(f'\nO aumento será de R$ {(15 / 100) * salario}, sendo assim o valor final e de {salario + (10 / 100) * salario}.')