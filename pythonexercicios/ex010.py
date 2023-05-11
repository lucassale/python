v = float(input('Quantos reais você tem na carteira? '))
d = v / 3.27
e = v / 5.2
print('Com R${} você pode trocar por: \nU${:.2f} ou \nE${:.2f}.'.format(v, d, e))