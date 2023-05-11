'''num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
num.sort(reverse=True)
num.insert(2, 2)
if 2 in num:
    num.remove(2)
else:
    print('Não achei o número 2')
print(num)
print(f'Essa lista tem {len(num)} elementos.')'''
valores = []
'''valores.append(1)
valores.append(2)
valores.append(3)'''
'''for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))'''

for c, v in enumerate(valores):
    print(f'Na posição {c} está o valor {v}!')
print(valores)
print('Cheguei no final da lista.')
a = [1, 2, 3, 4]
b = a[:]
b[2] = 10
print(f'A lista A: {a}')
print(f'A lista B: {b}')