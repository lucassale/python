v = (int(input('Digite um número: ')), int(input('Digite mais um número: ')),
     int(input('Digite outro número: ')), int(input('Digite o último número: ')))
print(v)
print(f'O número 9 aparece {v.count(9)} vezes.')
if 3 in v:
    print(f'O valor 3 aparece na {v.index(3) + 1}° posição.')
else:
    print('O valor 3 não aparece na tupla.')
c = 0
print('Os valores pares digitados foram: ', end='')
for n in v:
    c += 1
    if n % 2 == 0:
        print(f'{n} ', end='')
    else:
        if c == 4:
            print('<nenhum>')
