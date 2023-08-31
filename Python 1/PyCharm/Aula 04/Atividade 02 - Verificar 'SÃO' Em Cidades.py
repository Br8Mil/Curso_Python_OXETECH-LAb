nome = str(input('Digite o nome de uma cidade: ')).strip().upper()
nome_2 = nome.split()
print(f'{"SÃO" in nome_2[0]}')

#forma melhor
#cid = str(input('Digite o nome de uma cidade: ')).strip().upper()
#print(cid[:3] == 'SÃO')