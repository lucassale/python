'''nome = str(input('Qual é seuk nome? '))
if nome == 'Lucas':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))'''
n1 = float(input('Qual sua primeira nota: '))
n2 = float(input('Qual sua segunda nota: '))
m = (n1 + n2) / 2
print('Sua média foi {:.1f}'.format(m))
'''if m>=6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')'''
print('PARABÉNS!' if m >=6 else 'ESTUDE MAIS!')