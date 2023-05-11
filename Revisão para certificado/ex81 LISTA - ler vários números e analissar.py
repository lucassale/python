lista = []
s = 0
while True:
    lista.append(int(input('Digite um número: ')))
    s += 1
    r = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('Responsta inválida! Digite somente [S/N]. Quer continuar? ')).strip().upper()[0]
    if r == 'N':
        break
print('=-='*30)
print(f'a) A quantidade de valores digitados foram {s}.')
lista.sort(reverse=True)
print(f'b) A lista de valores em decrescente {lista}')
if 5 in lista:
    print(f'c) O valor 5 aparece nas posições: ', end='')
    for i, v in enumerate(lista):
        if v == 5:
            print(f'{i} ', end='')
else:
    print('c) O valor 5 não aparece na lista!')
