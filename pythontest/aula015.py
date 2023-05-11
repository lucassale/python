n = s = q = 0
n = int(input('Digite um número: '))
while True:
    s += n
    q += 1
    n = int(input('Digite um número: '))
    if n == 0:
        break
print(f'A quantidade de números foram {q} e soma dos número é igual a {s}.')