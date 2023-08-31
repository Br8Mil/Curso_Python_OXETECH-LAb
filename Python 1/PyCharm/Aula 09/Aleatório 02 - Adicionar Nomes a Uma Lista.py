lista = []
pergunta = 'S'

while pergunta != 'N':
    adicionar = str(input('\nDigite o nome da Pessoa que gostaria de adicionar: ')).strip().title()
    lista.append(adicionar)
    pergunta = str(input('\ngostaria de adicionar mais? [S/N]: ')).upper()[0]

print(lista)