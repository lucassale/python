s = float(input('Qual o salário do Funcionário? R$ '))
a = s * 0.15
nv = s + a
print('Um Funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(s, nv))