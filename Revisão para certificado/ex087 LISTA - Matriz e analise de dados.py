lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
s = sc = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        lista[l][c] = int(input(f'Digite um valor para a posição {l, c}: '))
print('=-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{lista[l][c]:^5}]', end='')
        if lista[l][c] % 2 == 0:
            s += lista[l][c]
    print()
for l in lista:
    sc += l[-1]
print(f'A soma dos valores pares é: {s}')
print(f'A soma dos valores da terceira coluna é: {sc}')
for c in range(0, 3):
    if c == 0:
        maior = lista[1][c]
    else:
        if lista[1][c] > maior:
            maior = lista[1][c]
print(f'A soma da segunda linha é: {maior}')

