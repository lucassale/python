from math import hypot
s = float(input('Digite o cateto oposto: '))
c = float(input('Digite o cateto adjacente: '))
h = hypot(c, s)#pode ser assim
hyp = (s**2 + c**2) **(1/2)#ou pode ser assim
print('Se o cateto oposto é {} \ne o cateto adjacente é {} então: \nA HIPOTENUSA será {:.2f}'.format(s, c, h))
print('A hipotenusa é {:.2f}'.format(hyp))
