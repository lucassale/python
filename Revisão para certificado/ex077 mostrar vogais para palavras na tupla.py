lista = ('Carlos', 'Lucas', 'Sales', 'Andrade')
for p in lista:
    print()
    print(f'Na palavra {p.upper()} temos as vogais ', end='')
    for l in p:
        if l.lower() in 'aeiou':
            print(l.lower(), end=' ')