def fatorial(n=1, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: É o número a ser calculado.
    :param show: É a opção de mostrar ou não a conta.
    :return: Retorno o valor do fatorial.
    """
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


print(fatorial(8, True))
help(fatorial)
