#Tuplas são imútaveis
lanche = ('hamburger', 'Suco', 'Pizza', 'Pudim')
print('\033[1;30m', lanche[-1:-5:-1], '\033[m')
print('=-=' * 15, end='\n')
for comida in lanche:
    print(f'\033[1;31mEu vou comer {comida};')
print('Nossa, comi pra caramba!\033[m')
print('=-=' * 15)
for cont in range(0, len(lanche)):
    print(f'\033[1;32mEu vou comer {lanche[cont]} na posição {cont}')
print('Nossa, comi pra caramba!\033[m')
print('=-=' * 15)
for pos, comida in enumerate(lanche):
    print(f'\033[1;33mEu vou comer {comida} na posição {pos}')
print('Nossa, comi pra caramba!\033[m')
print('=-=' * 15)
print(f'\033[1;34m', lanche)
print(sorted(lanche), '\033[m')
print('=-=' * 15)
print('\033[1;35mFIM\033[m')