input()
from random import randint
from time import sleep
from operator import itemgetter
jogador = {}
for j in range(1, 5):
    jogador[f'jogador{j}'] = randint(1, 6)
    jogador.copy()
print('VALORES SORTEADOS:')
for j, n in jogador.items():
    print(f'{"":<5}{j} tirou {n}')
    sleep(1)
ranking = []
ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)
print('RANKING DOS JOGADORES')
for i, v in enumerate(ranking):
    print(f'{"":<5}O {i+1}° lugar: {v[0]} com {v[1]}...')
    sleep(1)
print(jogador)
print(ranking)