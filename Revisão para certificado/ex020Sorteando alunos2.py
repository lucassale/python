from random import shuffle
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro auno: ')
a4 = input('Quarto aluno: ')
lista = [a1, a2, a3, a4]
print('A sequência escolhida foi: {}.'.format(lista, shuffle(lista)))
