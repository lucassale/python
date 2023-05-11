def contador(i, f, p):
    from time import sleep
    print('=-='*30)
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    print(f'A contagem de {i} até {f} de {p} em {p}')
    if i < f:
        while i < f:
            print(f'{i}', end=' ')
            i += p
        if i == f:
            print(f'{i}')
    if f < i:
        while i > f:
            print(f'{i}', end=' ')
            i -= p
        if i == f:
            print(f'{i}')
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
contador(int(input('Inicio: ')), int(input('Fim: ')), int(input('Passo: ')))