from random import randint

print('###Será que você consegue acertar o número que a máquina está pensado?###\nE um número entre 1 a 5.\n')
maquina = randint(1, 5)
nt = 0
pergunta = 0
while pergunta != maquina:
    pergunta = int(input('Digite um número entre 1 ou 5: '))
    if pergunta != maquina:
        print('O número não conincide com o da máquina, tente de novo.\n')
    nt = nt + 1

print(f'\n### ACERTOU MIZERAVI###\nO número de tentativas foi {nt}.')