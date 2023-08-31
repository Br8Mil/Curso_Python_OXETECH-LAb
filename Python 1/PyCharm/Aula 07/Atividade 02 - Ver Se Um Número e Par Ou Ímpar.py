# minha versão (ÍMPAR)
#num = 0
#escolha_1 = int(input('Digite até que número você deseja ir: '))
#escolha_2 = int(input('Digite o intervalo que deseja: '))
#for c in range(0, escolha_1, escolha_2):
    #soma = num + 1
    #if soma % 2:
        #print(f'O número {soma} e impar.')



# versão do professor (PAR)
num2 = int(input('Digite um número de INÍCIO: '))
num = int(input('Digite um número de FIM: '))
if num2 % 2 == 0:
    for c in range(num2, num+1, 2):
        print(c)
else:
    for c in range(num2+1, num+1, 2):
        print(c)