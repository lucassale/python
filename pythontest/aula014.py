n = 1
total = 0
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    total += n
    if n % 2 == 0 and n != 0:
        par += 1
    elif n != 0:
        impar += 1
print('A soma de todos é: {}'.format(total))
print('Temos {} pares e {} impares.'.format(par, impar))
