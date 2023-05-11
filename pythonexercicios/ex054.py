tma = 0
tme = 0
total = 0
for c in range(1, 8):
    ano = int(input('Quando nasceu a {}° pessoa? '.format(c)))
    if ano <= 2001:
        tma += 1
    else:
        tme += 1
total += c
print('Das {} datas;\n{} São maiores de idade;\n{} São menores de idade.'.format(total, tma, tme))
