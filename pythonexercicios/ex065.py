res = 'Ss'
soma = quant = média = maior = menor = 0
while res in 'Ss':
    num = int(input('Digite um número: '))
    quant += 1
    soma += num
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    res = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
média = soma / quant
print('Você digitou {} números e a média deles é {}.'.format(quant, média))
print('O MAIOR valor é {} e o MENOR é {}.'.format(maior, menor))
