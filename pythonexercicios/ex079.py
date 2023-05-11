valores = []
valores.append(int(input('Digite um valor: ')))
cont = 0
while True:
    cont += 1
    if cont > 1:
        if valores[-1] in valores[:cont-1]:
            print('Valor duplicado! Não vou adicionar...')
            valores.pop()
            cont -= 1
    r = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if r == 'N':
        break
    valores.append(int(input('Digite um valor: ')))
print('=-='*15)
print(f'O valores digitador foram: {sorted(valores)}')