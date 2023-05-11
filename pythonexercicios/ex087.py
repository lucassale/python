valores = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
total = maior = coluna3 = 0
for l in range(0, 3):
    for c in range(0, 3):
        valores[l][c] = int(input(f'Digite um valor para a [{l}, {c}]: '))
        if valores[l][c] % 2 == 0:
            total += valores[l][c]
        for c in range(0, 3):
            if c == 0:
                maior = valores[1][c]
            else:
                if valores[1][c] > maior:
                    maior = valores[1][c]
        if c == 2:
            coluna3 += valores[l][c]
print('=-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{valores[l][c]:^5}]', end=' ')
    print()
print('=-='*30)
print(f'A soma de todos os números é {total}.')
print(f'A soma dos números da coluna 3 é {coluna3}.')
print(f'O maior valor na linha 2 é {maior}.')