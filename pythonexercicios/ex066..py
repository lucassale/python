n = s = q = 0
while True:
    #s += n
    n = int(input('Digite um número: '))
    if n == 999:
        break
    q += 1
    s += n
print(f'Você digitou {q} número(s) e a soma dos números é {s}.')