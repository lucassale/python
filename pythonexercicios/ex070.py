print('-' * 30)
print('\033[1;36m     LOJÃO SUPER BARATO     \033[m')
print('-' * 30)
soma = alto = menor = quantidade = 0
nome = ''
while True:
    produto = str(input('Nome do produto: ')).strip()
    preço = float(input('Preço: R$'))
    soma += preço
    if preço > 1000:
        alto += 1
    if preço == 1:
        menor = preço
        nome = produto
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while resposta != 'S' and resposta != 'N':
        resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    print('=-=' * 10)
    if resposta == 'N':
        break
print('\n{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${soma} reais.')
print(f'Temos {alto} produtos custando mais de R$1000.00 reais.')
print(f'O produto mais barato foi a {nome} e custou {menor}')
