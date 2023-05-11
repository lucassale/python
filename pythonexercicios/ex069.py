print('CADASTRE UMA PESSOA')
print('---' * 10)
maior = mulheres = homens = 0
while True:
    idade = int(input('Idade: '))
    if idade > 18:
        maior += 1
    sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
        if sexo == 'M':
            homens += 1
        if sexo == 'F' and idade < 20:
            mulheres += 1
    print('=-=' * 10)
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resposta == 'N':
        break
    while resposta != 'N' and resposta != 'S':
        resposta = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    print('\nCADASTRE UMA PESSOA')
    print('---' * 10)
print('\n===', 'FIM DO PROGRAMA', '===')
print(f'O total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulheres} mulheres com menos de 20 anos.')
