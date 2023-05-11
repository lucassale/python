tupla = ('carlos', 'lucas', 'sales', 'andrade')
for p in tupla:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for v in p:
        if v.lower() in 'aeiou':
            print(v, end=' ')