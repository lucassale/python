lista = []
pares = []
impares = []
while True:
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('Resposta inválida...Quer continuar [S/N]? ')).strip().upper()[0]
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    if r == 'N':
        break
print('=-='*30)
print(f'A lista completa é {lista}...')
print(f'A lista de pares é {pares}...')
print(f'A lista de impares é {impares}...')