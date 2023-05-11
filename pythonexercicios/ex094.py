cadastro = []
dados = {}
soma = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
    while dados['sexo'] not in 'MF':
        dados['sexo'] = str(input('ERRO! Digite somente [M/F]: ')).upper().strip()[0]
        if dados['sexo'] in 'MF':
            break
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    cadastro.append(dados.copy())
    res = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    while res not in 'SN':
        res = str(input('ERRO! Digite somente [S/N]: ')).upper().strip()[0]
    if res == 'N':
        break
print('=-='*30)
print(cadastro)
print(f'{"A)"}Ao todo temos {len(cadastro)} cadastradas.')
media = soma/len(cadastro)
print(f'{"B)"}A média de idade é {media:.2f} anos.')
print(f'{"C)"}As mulheres cadastradas foram: ', end='')
for p in cadastro:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
print(f'\n{"D)"}A lista de pessoas que estão acima da média: ')
for p in cadastro:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<ENCERRADO>>')