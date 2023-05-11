print('Vamos ver quem é maior e quem é menor.')
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o tereiro valor: '))
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print('\033[0;32;40mO maior é {}.\033[m'.format(maior))
print('O menor é {}.'.format(menor))
