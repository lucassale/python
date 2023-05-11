from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
print('Pensei em um número inteiro entre 0 e 5.')
print('-=-' * 20)
jogador = int(input('Em que número pensei? '))
print('PROCESSANDO...')
sleep(5)
print('O número que pensei foi {} e não {}'.format(computador, jogador))
if jogador == computador:
    print('PARABÉNS! Você foi muito bem!')
else:
    print('Que pena você errou!')