from time import sleep
from emoji import emojize
print('=-'*5, 'CONTAGEM REGRESSIVA PARA FOGOS', '=-'*5)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
f1 = emojize('\033[31m:sparkler:\033[m')
f2 = emojize('\033[32m:sparkler:\033[m')
f3 = emojize('\033[33m:sparkler:\033[m')
for c in range(0, 5):
    print('\033[31m{} {} {}\033[m'.format(f1*5, f2, f3), end=' ')
    print('\033[32m{} {} {}\033[m'.format(f2*5, f1, f3), end=' ')
    print('\033[33m{} {} {}\033[m'.format(f3*5, f2, f1))
