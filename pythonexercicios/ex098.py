def contador(i=0, f=0, p=0):
    from time import sleep
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    while i < f:
        print(f'{i} ', end='')
        i += p
        sleep(0.5)
    while i >= f:
        print(f'{i} ', end='')
        i -= p
        sleep(0.5)
    print('FIM')
    print()


contador(1, 10, 1)
contador(10, 1, -2)
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)