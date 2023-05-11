def sortear(* num):
    from time import sleep
    from random import randint
    for c in range(1, 6):
        lista.append(randint(1, 10))
    print(f'A lista sorteada foi {lista}')


def somapar(* valores):
    soma = 0
    print('Os valores pares na lista é: ', end='')
    for v in lista:
        if v % 2 == 0:
            print(f'{v} ', end='')
            soma += v
    print()
    print(f'A soma dos números pares é {soma}.')


lista = []
sortear(lista)
somapar(lista)
