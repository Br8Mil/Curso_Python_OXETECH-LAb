tamanho = int(input('Nós diga o tamanho da parede em metros: '))
largura = int(input('Nós diga a sua largura em metros: '))
area = largura * tamanho
tinta = area / 2
print(f'\nA superfície de sua parede e igual a {area}m². Será necessário usar {tinta:,.2f} litros de tinta para pintar toda a parede')