'''from math import hypot
co = float(input('Qual o valor do cateto oposto: '))
ca = float(input('Qual o valor do cateto adjacente: '))
hip = hypot(co, ca)
print('O valor da hipotenusa é {:.2f}cm.'.format(hip))'''
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = (co** 2 + ca** 2) ** (1/2)
print('Se o cateto oposto é {} e o cateto adjacente é {}, então a hipotenusa é {:.2f}'.format(co, ca, hi))