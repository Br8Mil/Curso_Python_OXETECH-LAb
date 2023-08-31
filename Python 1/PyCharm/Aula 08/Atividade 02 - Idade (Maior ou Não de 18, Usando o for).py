from datetime import date
maior = 0
menor = 0
for c in range(1, 8):
    num = int(input(f'Digite a data de nascimento da {c}° pessoa: '))
    ano = date.today().year - num
    if ano >= 18:
        maior = maior + 1
    else:
        menor = menor + 1
print(f'Bem, ai existem {maior} de maior, é {menor} de menor.')