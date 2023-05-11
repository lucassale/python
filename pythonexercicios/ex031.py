viagem = float(input('Qual a distância da viagem? '))
p1 = (viagem * 0.5)
p2 = viagem * 0.45
if viagem <= 200:
    print('Sua passagem custará R${} reais'.format(p1))
else:
    print('Sua passagem custará R${}'.format(p2))
