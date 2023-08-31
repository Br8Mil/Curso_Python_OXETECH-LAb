primeiro = int(input('Digite o primeiro número: '))
segundo = int(input('Digite o segundo número : '))
terceiro = int(input('Digite o terceiro número: '))

maior = primeiro

if segundo > maior:
  maior = segundo
if terceiro > maior:
  maior = terceiro

menor = primeiro

if segundo < menor:
  menor = segundo
if terceiro < menor:
  menor = terceiro

print(f'A maior nota é {maior}, e a menor é {menor}.')