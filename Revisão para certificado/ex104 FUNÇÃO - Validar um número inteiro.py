def leiaInt(msg):
    print('-'*40)
    ok = False
    valor = 0
    while True:
        num = str(input(msg)).strip()
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('\033[1;31mERRO! Digite um número válido.\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Você acabou de digirar o número {n}')
