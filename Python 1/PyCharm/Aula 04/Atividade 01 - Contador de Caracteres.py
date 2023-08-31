nome = str(input('Digite o seu nome: ')).strip()
print(f'\nTudo em maiúsculo: {nome.upper()}\nTudo em minúsculo: {nome.lower()}')
separa = nome.split()
print(f'E possui {len(separa[0])} letras no primeiro nome, e {len(nome) - nome.count(" ")} caracteres no total.')