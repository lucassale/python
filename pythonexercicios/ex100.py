def sorteio(lista):
    from random import randint
    from time import sleep
    print('Analisandos os valores...')
    for c in range(0, 5):
        n = randint(1, 10)
        print(n, end=' ')
        lista.append(n)
        sleep(0.5)


def pares(lista):
    s = 0
    for v in lista:
        if v % 2 == 0:
            s += v
    print()
    print(f'Somando os valores pares em {lista} temos: {s} ')

lista = []
sorteio(lista)
pares(lista)

