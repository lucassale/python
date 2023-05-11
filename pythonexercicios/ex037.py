num = int(input('Digite um número: '))
print('''Escolha entre as opções abaixo:
[1] para BINÁRIO
[2] para OCTAL
[3] para HEXADECIMAL''')
escolha = int(input('Sua opção: '))
if escolha == 1:
    print('{} convertido para BINÁRIO é {}.'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('{} convertido para OCTAL é igual a {}.'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('{} convertido para HEXADECIMAL é igual {}.'.format(num, hex(num)[2:]))
else:
    print('Essa opção é INVÁLIDA, tente outra vez.')