import random
from time import sleep
print('PENSEI EM UM NÚMERO INTEIRO ENTRE 0 E 5')
n = int(input('Tente adivinhar qual: '))
print('*==*' * 5)
print('...PROCESSANDO...')
print('*==*' * 5)
sleep(3)
lista = [0, 1, 2, 3, 4, 5]
s = random.choice(lista)
print('Eu pensei no {}'.format(s))
if n == s :
    print('PARABENS! Você ganhou!')
else:
    print('KKK, EU GANHEI! Você perdeu!')
