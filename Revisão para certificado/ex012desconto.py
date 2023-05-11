print('PROMOÇÃO... Televisores com 5% de desconto.')
p = float(input('Temos televisores de R$ 999,90 e 1590,90. Qual você prefere? '))
d = p - (p * 0.05)
print('A televisão que custava R${:.2f}, com desconto de 5% sairá por R${:.2f}'.format(p, d))
