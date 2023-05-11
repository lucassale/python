media = 0
ihv = 0
nhv = ''
totalm = 0
for p in range(1, 5):
    print('----- {}° PESSOA -----'.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    media += idade / 4
    if p == 1 and sexo in 'Mm':
        ihv = idade
        nhv = nome
    if sexo in 'Mm' and idade > ihv:
        ihv = idade
        nhv = nome
    if sexo in 'Ff' and idade < 20:
        totalm += 1
print('A média de idade é: {:.1f} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(ihv, nhv))
print('Ao todo tem {} mulher(es) com menos de 20 anos.'.format(totalm))
