from random import randint
from time import sleep
print('=-='*15)
print(f'{"JOGOS DA MEGA SENA":^45}')
print('=-='*15)
j = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-= SORTENADO {j} JOGOS -=-=')
lista = []
jogo = []
jogos = 1
while jogos <= j:
    cont = 0
    while cont <= 6:
        n = randint(1, 60)
        if n not in jogo:
            jogo.append(n)
            cont += 1
    jogo.sort()
    lista.append(jogo[:])
    jogo.clear()
    jogos += 1
for i, v in enumerate(lista):
    print(f'Jogo {i+1}: {v}')
    sleep(0.5)
print('-=-=-= <BOA SORTE!> -=-=-=')