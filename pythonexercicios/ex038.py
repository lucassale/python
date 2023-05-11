from time import sleep
print('#' * 5, '\033[32mANALISANDO números inteiros como MAIOR OU IGUAL\033[m', '#' * 5)
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
print('ANALISANDO')
sleep(3)
if n1 > n2:
    print('\033[35m{}\033[m é maior que \033[36m{}\033[m'.format(n1, n2))
elif n2 > n1:
    print('\033[31m{}\033[m é maior que \033[32m{}\033[m'.format(n2, n1))
else:
    print('\033[34m{} e {}\033[m são iguais.'.format(n1, n2))
