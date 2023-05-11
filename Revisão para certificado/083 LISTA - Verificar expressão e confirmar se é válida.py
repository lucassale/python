lista = str(input('Digite uma expressão: '))
d = e = 0
for v in lista:
    if v == '(':
        e += 1
    elif v == ')':
        d += 1
print('=-='*30)
print(e)
print(d)
if e == d:
    print('A expressão é válida!')
else:
    print('A expressão não é válida!')