print('Quer saber quantos dólares você pode comprar?')
c = float(input('Quanto você tem na carteira? '))
ct = float(3.27)
print('Com {}R$ reais, você pode comprar {}$ dólares'.format(c, (c / ct)))