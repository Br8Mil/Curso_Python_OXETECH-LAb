sexo = 'a'
while sexo not in 'MF':
    sexo = str(input('Digite seu sexo: [M/F] ')).upper().strip()[0]
    if sexo == 'M':
        print('O sexo escolhido foi masculino.')
    elif sexo == 'F':
        print('O sexo escolhido foi feminino.')
    else:
        print('Comando inválido, tente novamente.')


