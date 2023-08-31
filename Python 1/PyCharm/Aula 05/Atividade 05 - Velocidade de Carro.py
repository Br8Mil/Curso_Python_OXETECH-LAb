velocidade = float(input('Digite a velocidade que o carro estava: '))
if velocidade <= 80.0:
    print('\nSeu carro está dentro do limite de velocidade, meus parabéns por ser um motorista consciente.')
else:
    print(f'''\nO seu veículo está acima do limite de velocidade.
você utrapassou {velocidade - 80.00} Km/h acima do permitido e deve pagar uma multa que corresponde a R$ 7.00 por
quilômetro ultrapassado.

Sendo assim sua multa será de R${(velocidade - 80.00) * 7.00:,.2f}, ande mais devagar da próxima.''')