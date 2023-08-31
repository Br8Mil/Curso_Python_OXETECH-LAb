soma = qv = 0
while True:
    num = int(input('Digite um valor: '))
    if num == 999:
        break
    soma = soma + num
    qv = qv + 1
print(f'\nA quantidade de vezes foi de {qv}.\nÉ a soma de todos os números digitados foi {soma}.')
