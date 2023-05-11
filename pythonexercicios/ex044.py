preço = float(input('Qual o valor das compras? '))
print('Como ver deseja pagar este produto? Escolha uma das opções abaixo.')
print('''[1] - À vista em dinheiro ou cheque.
[2] - À vista no cartão.
[3] - 2x no cartão.
[4] - 3x ou mais no cartão.''')
e = int(input('Digite a sua opção entre 1 e 4: '))
if e == 1:
    d = preço - (preço * 0.10)
    print('\nPagando à vista no dinheiro ou cheque você terá 10% de desconto.')
    print('Sua compra de R${:.2f} sairá por R${:.2f}.'.format(preço, d))
elif e == 2:
    d = preço - (preço * 0.05)
    print('\nPagando à vista no cartão seu desconto será de 5%.')
    print('Sua compra de R${:.2f} sairá por R${:.2f}.'.format(preço, d))
elif e == 3:
    print('\nParcelando em 2x Você pagará o preço normal do produto.')
    print('Sua compra não terá desconto e sairá por R${:.2f}.'.format(preço))
elif e == 4:
    a = preço + (preço * 0.2)
    v = int(input('Em quantas vezes quer parcelar? '))
    print('Parcelando em {}x você pagará {} por parcela e o valor total será R${:.2f}.'.format(v, a / v, a))
else:
    print('\033[1;31mOPÇÃO INVÁLIDA, ESCOLHA ENTRE 1 E 4 POR FAVOR.\033[m')
