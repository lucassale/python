print('=*=' * 5, 'GERANDO UMA PA', '=*=' * 5)
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
total = 0
while total != 10:
    print('{} -> '.format(p), end='')
    p += r
    total += 1
print('FIM')