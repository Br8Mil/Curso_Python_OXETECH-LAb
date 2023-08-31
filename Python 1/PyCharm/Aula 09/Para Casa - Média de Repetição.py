sn = 'S'
soma = 0
contador = 1
lista = []

while sn != 'N':
    pergunta = int(input(f'\nDigite o {contador}° valor: '))
    soma = soma + pergunta
    contador = contador + 1
    lista.append(pergunta)
    pergunta_2 = str(input('\nvocê gostaria de adicionar mais números? [S/N]: ')).upper().strip()[0]
    if pergunta_2 == 'S':
        pass
    elif pergunta_2 == 'N':
        sn = 'N'
    else:
        print('\nEsta não e uma opção válida.')

print(
    f'\nEsses são os valores que você digitou {lista}.\nA média dos números digitados é: {soma / contador}.\nO maior número é: {max(lista, key=int)}.\nO menor número é: {min(lista, key=int)}')