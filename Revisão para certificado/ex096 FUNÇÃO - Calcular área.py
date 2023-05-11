def área(a, b):
    area = a * b
    print('-' * 60)
    print(f'A área de um terreno com as medidas {a:.2f}mx{b:.2f}m mede {area}m².')
    print('-' * 60)


print('CALCULO DE ÁREA')
a = float(input('Digite a altura: '))
b = float(input('Digite a largura: '))
área(a, b)
