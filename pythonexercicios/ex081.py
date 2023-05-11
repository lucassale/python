lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('Resposta inválida...Quer continuar [S/N]? ')).strip().upper()[0]
    if r == 'N':
        break
print(f'Você digitou {len(lista)} elementos...')
lista.sort(reverse=True)
print(f'A sua lista é {lista}...')
if 5 in lista:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 não esta na lista!')
