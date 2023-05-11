def área(l, c):
    area = l * c
    print(f'Uma área de {l}x{c} mede {area}m².')


print('CONTROLE DE TERRENOS')
print('=-='*10)
l = float(input('Largura(m): '))
c = float(input('Comprimento(m): '))
área(l, c)
