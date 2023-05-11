from random import randint
valores = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(valores)
print(f'O maior valor é {max(valores)} na posição {valores.index(max(valores))+1}')
print(f'O menor valor é {min(valores)} na posição {valores.index(min(valores))+1}')
