valores = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        valores[l][c] = int(input(f'Digite um valor para a [{l}, {c}]: '))
    print(valores)
print('=-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{valores[l][c]:^5}]', end=' ')
    print()
    