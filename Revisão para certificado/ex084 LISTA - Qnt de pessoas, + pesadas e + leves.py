pessoas = []
dados = []
total = maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    total += 1
    dados.append(int(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    r = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('Responsta inválida! Quer continuar [S/N]? ')).strip().upper()[0]
    if r == 'N':
        break
for i, p in enumerate(pessoas):
    if i == 0:
        maior = p[1]
        menor = p[1]
    else:
        if p[1] > maior:
            maior = p[1]
        if p[1] < menor:
            menor = p[1]
print('=-='*30)
print(f'Foram cadastradas {total} pessoas.')
print(f'O maior peso foi de {maior}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]} ', end='')
print(f'\nO menor peso foi de {menor}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]} ', end='')
