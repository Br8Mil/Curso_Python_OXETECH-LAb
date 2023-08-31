from random import randint
n = 0
lista = []
while n <= 5:
    na = randint(1, 100)
    lista.append(na)
    n = n + 1
print(f'Os números esolhidos foram {lista}\nO maior número é {max(lista)}.\nÉ o menor é {min(lista)}.')