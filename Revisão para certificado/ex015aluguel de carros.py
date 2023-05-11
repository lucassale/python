km = float(input('Quantos km você percorreu? '))
dias = int(input('Por quantos dias você alugol? '))
#valor = (km * 0.15) + (dias * 60)
#print('Se você rodou {}km e alugou por {} dias, você deverá pagar R${}'.format(km, dias, valor))
k = km * 0.15
d = km * 60
print('Você irá pagar R${} reis pela quilometragem.\nE R${} reais pelos dias alugados'.format(k, d))
print('Seu custo total será R${}'.format((k) + (d)))
