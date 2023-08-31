numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Quinto', 'Sexto', 'Sétimo', 'Oitavo', 'Nono', 'Décimo')
while True:
    num = int(input('Digite um número entre 0 e 10: '))
    if num in range(0, 10):
        print(f'\nVocê digitou o {numeros[num]} número.\n')
        break
    print('###ENTRE 0 e 10.###\n')