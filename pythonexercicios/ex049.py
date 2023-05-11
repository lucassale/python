tabuada = int(input('Escolha o número para saber a tabuada: '))
for c in range(1, 10 + 1):
    print('{} x {:2} = {:2}'.format(tabuada, c, tabuada * c))
