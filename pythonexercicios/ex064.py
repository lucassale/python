n = total = soma = 0
n = int(input('Digite um valor ou [999 para encerrar]: '))
while n != 999:
    total += 1
    soma += n
    n = int(input('Digite um valor ou [999 para encerrar]: '))
print('Você digitou {} valores e a soma deles é {}.'.format(total, soma))
