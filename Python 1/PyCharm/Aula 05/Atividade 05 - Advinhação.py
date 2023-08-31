import random
numero = random.randint(1, 5)
pergunta = int(input('Estou pensado em um número entre 1 ou 5. você consegue advinhar?: '))
if numero == pergunta:
    print(f'\nParabéns você acertou, eu realmente estava pensado no número {numero}')
else:
    print(f'\nVocê errou, eu estava pesnado no número {numero}.')