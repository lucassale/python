lista = [[], []]
for c in range(1, 8):
    n = (int(input(f'Digite o {c}° valor: ')))
    if n % 2 == 0:
        lista[0].append(n)
        lista[0].sort()
    else:
        lista[1].append(n)
        lista[1].sort()
print('=-='*30)
print(f'Os valores pares são {lista[0]}')
print(f'Os valores impares são {lista[1]}')
