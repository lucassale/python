def fatorial(n, show=True):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c} ', end='')
            if c > 1:
                print('x ', end='')
            else:
                print('= ', end='')
        f *= c
    return f


print(fatorial(6))
