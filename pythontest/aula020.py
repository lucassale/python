'''def l():
    print('-'*20)


# Programa principal
l()
print(f'{"Carlos":^20}')
l()
l()
print(f'{"Lucas":^20}')
l()
l()
print(f'{"Sales":^20}')
l()
l()
print(f'{"Andrade":^20}')
l()'''


'''def m(msg):
    print('-'*50)
    print(msg)
    print('-'*50)


m(f'{"CARLOS":^50}')
m(f'{"LUCAS":^50}')
m(f'{"SALES":^50}')
m(f'{"ANDRADE":^50}')'''


'''def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma entre A + B = {s}')


# Programa printcipal
from random import randint
par = soma((int(input('Número A: '))), (int(input('Número B: '))))
soma(2, 4)
soma(3, 5)
aleatório = soma((randint(1, 5)), (randint(1,5)))
soma(2*4, 3*5)'''

'''def contador(*num):
    tamanho = len(num)
    print(f'A tupla {num} tem {tamanho} valores.')


contador(1, 2, 3, 4, 5)
contador(10, 9, 8)
contador(20, 30, 50, 40)'''


def dobra(valores):
    pos = 0
    while pos < len(valores):
        valores[pos] *= 2
        pos += 1


valores = [1, 2, 3, 4, 5]
dobra(valores)
print(valores)