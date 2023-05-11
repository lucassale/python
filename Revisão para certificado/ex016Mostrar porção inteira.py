from math import floor, trunc
num = float(input('Digite um número: '))
i = floor(num)
#i2 = num // 1 também funciona assim!
t = trunc(num)
print('A divisão inteira de {} é {}.'.format(num, i))
print('A divisão inteira é {}'.format(trunc(num)))
print('A divisão inteira é {}'.format(int(num)))

