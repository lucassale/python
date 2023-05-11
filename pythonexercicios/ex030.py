num = int(input('Digite um número inteiro: '))
resultado = num % 2
if resultado == 0:
    print('O número {} é PAR.'.format(resultado))
else:
    print('O número {} é IMPAR.'.format(resultado))