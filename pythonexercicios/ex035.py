print('Escreva abaixo três medidas de retas que formem um triângulo:')
a = float(input('Primeira reta: '))
b = float(input('Segunda reta: '))
c = float(input('Terceira reta: '))
if (a - b) < c < a + c and (a - c) < b < a + c or (b - c) < a < b + c:
    print('PARABENS!!! Essas 3 retas fomam um triângulo.')
else:
    print('Que pena essas 3 retas não formam um triângulo.')