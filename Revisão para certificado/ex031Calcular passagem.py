viagem = float(input('Qual a distância da sua viagem? '))
print('Viagens até 200km custam R$0.50 centavos p/cada km e R$0.45 centavos para viagens acima de 200km.')
if viagem <= 200:
    print('Sua passagem custará: R${:.2f} reais'.format(viagem * 0.5))
else:
    print('Sua viagem custará: R${:.2f} reais'.format(viagem * 0.45))
