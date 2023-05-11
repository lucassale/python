print('-' * 20)
print('BANCO CEV')
print('-' * 20)
valor = int(input('Quanto você quer sacar? '))
saque = valor
ced = 50
totalced = 0
while True:
    if saque >= ced:
        saque -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédula(s) de R${ced}.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if saque == 0:
            break