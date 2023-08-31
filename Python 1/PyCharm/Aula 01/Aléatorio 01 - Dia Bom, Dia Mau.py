nome = input('Seu nome é? ')
bom = ('\nOba, e muito bom saber disso.')
mau = ('\nQue pena, mas lembre se esses dias passam.')
correcao = ('''\n\n###Ei, Mal é advérbio, antônimo de bem. Mau é um adjetivo, antônimo de bom.

    Exemplos: O funcionário apresentou um mau desempenho, por isso foi afastado. (mau ≠ bom)

              Os alunos foram mal na prova porque estudaram pouco. (mal ≠ bem).''')

pergunta = input('\nComo está seu dia? bom ou mau? ')

pergunta = pergunta.upper()

if pergunta == 'BOM':
    print(bom)

elif pergunta == 'MAU':
    print(mau)

elif pergunta == 'MAL':
    print(f'{mau} {correcao}')

else:
    print('''Hum, você digitou algo que eu não entendi, como este é um programa simples
   ele vai parar por aqui, porém você pode reiniciar e tentar novamente

   ###tente responder com bom ou mal###.''')