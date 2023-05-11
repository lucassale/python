pessoa = {}
cad = []
smédia = média = 0
while True:
    pessoa['nome'] = str(input('Nome: ')).strip().capitalize()
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while pessoa['sexo'] not in 'MF':
        print('Erro! Por favor digite somente [M/F].')
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    smédia += pessoa['idade']
    res = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    while res not in 'SN':
        print('Erro! Por favor digite somente [S/N]')
        res = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    cad.append(pessoa.copy())
    if res == 'N':
        break
print('=-='*30)
print(f'A) Ao todo temos {len(cad)} pessoas cadastradas.')
média = smédia / len(cad)
print(f'B) A média de idade é de {média:.2f} anos.')
print(f'C) A mulheres cadastradas fora: ', end=' ')
for p in cad:
    if p['sexo'] in 'F':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média:')
for p in cad:
    if p['idade'] > média:
        print(f'    nome {p["nome"]}; sexo = {p["sexo"]}; idade = {p["idade"]};')