from random import randint
print('=-=' * 10)
print('VAMOS BRINCAR DE \033[1;4;32mPAR\033[m OU \033[1;4;31mÍMPAR\033[m')
print('=-=' * 10)
par = 'PAR'
impar = 'ÍMPAR'
jogador = ''
soma = vitoria = perda = 0
while True:
    soma = 0
    computador = randint(0, 10)
    jogador = int(input('\nDigite um valor: '))
    escolha = str(input('Escolha PAR ou ÍMPAR [P/I]: ')).strip().upper()
    soma += jogador + computador
    if escolha == 'P' and soma % 2 == 0:
        print(f'Você escolheu {jogador} e o computador {computador}. A soma é {soma} e deu {par}.')
        print('Você GANHOU!!!')
        vitoria += 1
        print('Vamos jogar novamente...')
        print('=-=' * 10)
    if escolha == 'P' and soma % 2 == 1:
        print(f'Você esolheu {jogador} e o computador {computador}. A soma é {soma} e deu {impar}.')
        print('Você perdeu!!!')
        perda += 1
    if escolha == 'I' and soma % 2 == 1:
        print(f'Você esolheu {jogador} e o computador {computador}. A soma é {soma} e deu {impar}.')
        print('Você GANHOU!!!')
        vitoria += 1
    if escolha == 'I' and soma % 2 == 0:
        print(f'Você esolheu {jogador} e o computador {computador}. A soma é {soma} e deu {par}.')
        print('Você PERDEU!!!')
        perda += 1
    if perda > 0:
        break
print('=-=' * 10)
print(f'\nGAME OVER! Você acertou {vitoria} vezes antes de perder.')
