print('=-=' * 5, '\033[1;34mTABUADAS\033[m', '=-=' * 5)
num = int(input('Digite um número para saber a tabuada: '))
i = 1
quantidade = 0
while True:
    print(f'{num} x {i} = {num * i}')
    i += 1
    if i == 11:
        i = 1
        num = int(input('Digite um número para saber a tabuada: '))
    if num <= 0:
        break
print('Número inválido, progama encerrado.')