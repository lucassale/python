dados = []
pessoas = []
pesados = []
leves = []
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    r = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('Resposta inválida... Quer continuar [S/N]? ')).strip().upper()[0]
    if r == 'N':
        break
for p in pessoas:
    if p[1] > 100:
        pesados.append(p[0])
    elif p[1] < 80:
        leves.append(p[0])
print('=-='*30)
print(f'Temos {len(pessoas)} pessoas cadastradas.')
print(f'As pessoas acima de 100kg são: {pesados}')
print(f'As pessoas abixo de 80kg são: {leves}')
