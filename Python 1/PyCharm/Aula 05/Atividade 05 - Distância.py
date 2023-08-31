pergunta = float(input('Quantos quilômetros a sua viagem terá?: '))
if pergunta <= 200:
    print(f'\nSua passagem custará R$ {pergunta * 0.50:,.2f}.')
else:
    print(f'\nSua passagem custará R$ {pergunta * 0.45:,.2f}.')