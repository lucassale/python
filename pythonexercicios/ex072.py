ext = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if n < 0 or n > 20:
        print('Número inválido...')
        print('\nTente novamente...', end='')
    elif n >= 0 or n <= 20:
        print(f'Você digitou {ext[n]}')
        r = str(input('Você quer continuar? ')).strip().upper()[0]
        while r not in 'SN':
            r = str(input('Você quer continuar? ')).strip().upper()[0]
        if r == 'N':
            break
        elif r == 'S':
            print('Vamos de novo...')
