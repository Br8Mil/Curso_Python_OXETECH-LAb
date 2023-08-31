nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
print()

media = (nota1 + nota2) / 2

if media == 10.0:
    print('O aluno foi aprovado com nota máxima.')
elif media < 5.0:
    print('O aluno foi reprovado.')
elif media >= 7.0:
    print('O aluno atingiu a média nescessaria para passar.')
else:
    media <= 6.9 and 5.0
    print ('O aluno está em recuperação.')
print(f'Ele possui uma média de {media} pontos')