import random
import time
print('Vamos jogar JOKENPO. Se sabe as regras, vamos lá!')
escUser = str(input('Escolha PEDRA, PAPEL OU TESOURA: ')).lower().strip()
joken = ['pedra','papel','tesoura']
escComp = random.choice(joken)
time.sleep(1)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('POOOOOOO')

print(f'A escolha da máquina foi: {escComp.upper()}')
if escUser == 'pedra':
    if escComp == 'pedra':
        print('Empatou...')
    elif escComp == 'papel':
        print('Perdeu.')
    elif escComp == 'tesoura':
        print('VOCÊ GANHOU!!!')

elif escUser == 'tesoura':
    if escComp == 'pedra':
        print('Perdeu.')
    elif escComp == 'papel':
        print('GANHOU!!!')
    elif escComp == 'tesoura':
        print('Empatou...')

elif escUser == 'papel':
    if escComp == 'pedra':
        print('GANHOU!!!')
    elif escComp == 'papel':
        print('Empatou...')
    elif escComp == 'tesoura':
        print('Perdeu.')