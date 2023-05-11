from random import randint
print('''Sou seu computador e pensei em um número entre 0 e 10.
Será que você consegue adinvinhar?''')
acertou = False
palpites = 0
computador = randint(0, 10)
while not acertou:
    jogador = int(input('Digite seu palpite: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print('MENOS...')
        elif jogador < computador:
            print('MAIS...')
print('Você acertou com {} tentativas. PARABÉNS!!!'.format(palpites))
