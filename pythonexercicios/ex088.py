from random import randint
from time import sleep
print('=-='*10)
print(f'{"JOGOS DA MEGA SENA":^25}')
print('=-='*10)
lista = []
jogos = []
quant = int(input('Qantos jogos você quer que eu sorteie? '))
total = 1
while total <= quant:
    cont = 0
    while True:
        n = randint(1, 60)
        if n not in jogos:
            jogos.append(n)
            cont += 1
        if cont >= 6:
            break
    jogos.sort()
    lista.append(jogos[:])
    jogos.clear()
    total += 1
print(f'{"SORTEANDO":-^50}')
for i, j in enumerate(lista):
    print(f'JOGO {i+1}: {j}')
    sleep(1)
print(f'{"BOA SORTE":-^50}')