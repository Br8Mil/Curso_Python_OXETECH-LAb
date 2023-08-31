import time

virgula = (',')

print('### BEM VINDO A CALCULADORA DE IDADE ###\n\nvamos começar pedindo algumas informaçoẽs.\n')

nome = input('Digite o seu nome: ')

ano1 = int(input('\nDigite o ano atual: '))

print('\nBeleza, agora gostaríamos de saber o dia, mês e ano em que você nasceu:\n')

dia2 = int(input('Digite o dia: '))
if dia2 <= 31:
    pass
else:
    print('\nUm mês possui no máximo 31 dias.\n\n##ERRO FATAL##\n\nO programa será fechado em 10 segundos.\n')
    time.sleep(10)
    exit()

print('\nEscolha o seu mês de nasciemento:\n\n[1] - Janeiro\n[2] - Fevereiro\n[3] - Março\n[4] - Abril\n[5] - Maio\n[6] - Junho\n[7] - Julho\n[8] - Agosto\n[9] - Setembro\n[10] - Outubro\n[11] - Novembro\n[12] - Dezembro')
  
mes2 = int(input('\nDigite o número correspondente: '))
if mes2 <= 12:
    pass
else:
    print('\nEste número não está nas alternativas.\n\n##ERRO FATAL##\n\nO programa será fechado em 10 segundos.\n')
    time.sleep(10)
    exit()

ano2 = int(input('\nDigite o ano: '))

f1 = (ano1 - ano2 - 1)


if mes2 == 1:
    print('\nBem', nome + virgula, 'você possui', f1, 'anos', 'e', 365 - dia2 + 31, 'dias')
elif mes2 == 2:
     print('\nBem', nome + virgula, 'você possui', f1, 'anos', 'e', 365 - dia2 + 59, 'dias')
elif mes2 == 3:
      print('\nBem', nome + virgula, 'você possui', f1, 'anos', 'e', 365 - dia2 + 90, 'dias')
elif mes2 == 4:
     print('\nBem', nome + virgula, 'você possui', f1, 'anos', 'e', 365 - dia2 + 120, 'dias')
elif mes2 == 5:
     print('\nBem', nome + virgula, 'você possui', f1, 'anos', 'e', 365 - dia2 + 151, 'dias')
elif mes2 == 6:
    print('\nBem', nome + virgula, 'você possui', f1, 'anos', 'e', 365 - dia2 + 181, 'dias')
elif mes2 == 7:
     print('\nBem', nome + virgula, 'você possui', f1, 'anos', 'e', 365 - dia2 + 212, 'dias')
elif mes2 == 8:
     print('\nBem', nome + virgula, 'você possui', f1, 'anos', 'e', 365 - dia2 + 243, 'dias')
elif mes2 == 9:
    print('\nBem', nome + virgula, 'você possui', f1, 'anos', 'e', 365 - dia2 + 273, 'dias')
elif mes2 == 10:
     print('\nBem', nome + virgula, 'você possui', f1, 'anos', 'e', 365 - dia2 + 304, 'dias')
elif mes2 == 11:
      print('\nBem', nome + virgula, 'você possui', f1, 'anos', 'e', 365 - dia2 + 334, 'dias')
elif mes2 == 12:
    print('\nBem', nome + virgula, 'você possui', f1, 'anos', 'e', 365 - dia2, 'dias')
else:
  pass

print("\nNote que esta calculadora, não leva em conta os dias do anos bisextos")
