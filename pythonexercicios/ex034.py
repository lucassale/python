valor = float(input('Qual o salário do funcionário? '))
'''a1 = (valor * 0.1) + valor
a2 = (valor * 0.15) + valor'''
if valor >= 1250:
    novo = valor + (valor * 0.1)
else:
    novo = valor + (valor * 0.15)
print('Seu novo salário será de: R${:.2f} reais'.format(novo))
