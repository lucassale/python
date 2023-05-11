compras = ('lapis', 1.00, 'caderno', 15.00, 'tablet', 1500.00)
print('-' * 40)
print(f'{"LISTA DE COMPRAS":^40}')
print('-' * 40)
for c in range(0, len(compras)):
    if c % 2 == 0:
        print(f'{compras[c]:.<30}', end='')
    elif c % 2 == 1:
        print(f'R${compras[c]:>7.2f}')
print('-' * 40)