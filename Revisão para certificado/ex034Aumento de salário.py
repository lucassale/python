s = float(input('Digite seu salário: '))
a1 = (s * 0.15) + s
a2 = (s * 0.10) + s
if s >= 1250:
    print('Seu novo salário será: R${:.2f}'.format(a2))
else:
    print('Seu novo salário será: R${:.2f}'.format(a1))
