lista = []
while True:
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não irei adicionar...')
    print(lista)
    res = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while res not in 'SN':
        res = str(input('Resposta inválida! Quer continuar? [S/N] ')).strip().upper()[0]
    if res == 'N':
        break
print('=-='*30)
lista.sort()
print(f'Você digitou os valores {lista}')
