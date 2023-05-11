from random import randint
from time import sleep
from operator import itemgetter
jog = {}
for c in range(1, 5):
    jog[f'jogador{c}'] = randint(1, 6)
print('SORTENADO NÚMEROS...')
for k, v in jog.items():
    sleep(1)
    print(f'{k} tirou {v}')
print('=-='*30)
ranking = []
ranking = sorted(jog.items(), key=itemgetter(1), reverse=True)
print('     RANKING DOS JOGADORES...     ')
for i, v in enumerate(ranking):
    sleep(1)
    print(f' {i+1}° lugar: {v[0]} tirou {v[1]}')