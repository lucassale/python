num = int(input('Digite um número: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m{}'.format(c), end=' ')
        total += 1
    else:
        print('\033[31m{}'.format(c), end=' ')
if total == 2:
    print('\n\033[mO número {} é divisivel por {} números, portanto é PRIMO!'.format(num, total))
else:
    print('\n\033[mO número {} é divisível por {} números, portanto NÃO é PRIMO!'.format(num, total))
