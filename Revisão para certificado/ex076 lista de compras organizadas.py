print('=-='*15)
print(f'{"LISTA DE PREÇOS":^40}')
print('=-='*15)
lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Mochila', 120.00)
print('-'*40)
for i, v in enumerate(lista):
    if i % 2 == 0:
        print(f'{v:.<8}{"":.>20}', end='')
    else:
        print(f'{"R$":>}{v:>7.2f}')
print('-'*40)