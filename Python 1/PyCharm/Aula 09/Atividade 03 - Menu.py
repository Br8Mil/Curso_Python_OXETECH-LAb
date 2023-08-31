p1 = float(input('Digite o 1º valor: '))
p2 = float(input('Digite o 2º valor: '))
op = 0

while op != 5:
    op = float(input('O que você quer fazer?\n\n[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS NÙMEROS\n[5] SAIR DO PROGRAMA\nE ai, qual escolhe? '))
    if op == 1:
        soma = p1 + p2
        print(f'A soma deu {soma}.\n')
    elif op == 2:
        multi = p1 + p2
        print(f'A multiplicação deu {multi}.\n')
    elif op == 3:
        if p1 > p2:
            print(f'{p1} e maior do que {p2}.\n')
        else:
            print(f'{p2} e maior do que {p1}.\n')
    elif op == 4:
        p1 = float(input('\nDigite o 1º valor: '))
        p2 = float(input('\nDigite o 2º valor: '))
    else:
        print('###\nNúmero inválido, tente de novo.###\n')

print('\nObrigado por usar o programa.')
