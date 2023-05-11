print('Vou te ajudar a comprar a quantidade de tinta.')
a = float(input('Qual a altura da sua parede? '))
l = float(input('Qual a largura da sua parede? '))
m = (a * l)
t = m / 2
print('Sua parede mede {}m² , portanto precisará de {:.2f} litros de tinta'.format(m, t))
