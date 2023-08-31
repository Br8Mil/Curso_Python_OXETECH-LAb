times = ('Palmeiras', 'Botafogo', 'Fluminense', 'Athetico-PR', 'Cruzeiro', 'Fortaleza',
         'São Paulo', 'Atlético-MG', 'Santos', 'Grêmio', 'Internacional', 'Flamengo',
         'Bahia', 'Bragantino', 'Vasco da Gama', 'Corinthians', 'Cuiabá', 'Goiás',
         'América-MG','Coritiba')

print(f'\nOs 5 primeiros times são {times[0:5]}.E os últimos 5 são {times[-5:]}.\n\n'
    f'Em ordem alfabetica {sorted(times)}.\n\nEm que posição está o Vasco da Gama?, ele está na {times.index("Vasco da Gama") + 1}º posição.')