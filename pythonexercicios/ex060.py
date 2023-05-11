n = int(input('Digite um número inteiro para saber o seu FATORIAL: '))
f = 1
c = n
print('O FATORIAL DE {}! é: '.format(n), end='')
while c > 0:    #for n in range(n, 0, -1):
    print('{}'.format(c), end='')
    print('x' if c > 1 else '=', end='')
    f *= c
    c -= 1
print('{}'.format(f))
