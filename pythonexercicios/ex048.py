s = 0
cont = 0
for c in range(3, 500, 2):
    if c % 3 == 0:
        s += c
        cont += 1
print('\nO somatório dos {} números ímpares múltiplos de 3 entre 0 e 500 é {}'.format(cont, s))
