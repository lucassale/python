n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
print('Escolha o que deseja fazer com esses valores;')
r = 1
while r != 5:
    r = int(input('''MENU
[1] - SOMAR
[2] - MULTIPLICAR
[3] - MAIOR
[4] - NOVOS NÚMEROS
[5] - SAIR DO PROGRAMA
Digite a opção desejada: '''))
    if r == 1:
        print('A soma dos dois valores é igual: {}\n'.format(n1 + n2))
    elif r == 2:
        print('A multiplicação dos dois valores é igual: {}\n'.format(n1 * n2))
    elif r == 3:
        if n1 > n2:
            print('O Primeiro valor é o MAIOR.\n')
        elif n1 == n2:
            print('Os dois valores são iguais.\n')
        else:
            print('O Segundo valor é o MAIOR.\n')
    elif r == 4:
        print('Escolha novos valores;\n')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
if r == 5:
    print('VOCÊ SAIU DO PROGRAMA.')
