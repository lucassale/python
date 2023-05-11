import emoji
from random import choice
from time import sleep
print(emoji.emojize(':oncoming_fist_light_skin_tone::raised_back_of_hand_light_skin_tone::victory_hand_light_skin_tone:\033[1;32;40mJOKENPÔ\033[m:oncoming_fist_light_skin_tone::raised_back_of_hand_light_skin_tone::victory_hand_light_skin_tone:'))
pedra = emoji.emojize(':oncoming_fist_light_skin_tone:')
papel = emoji.emojize(':raised_back_of_hand_light_skin_tone:')
tesoura = emoji.emojize(':victory_hand_light_skin_tone:')
computador = choice([pedra])
jogador = str(input('Digite sua escolha entre "PEDRA", "PAPEL" e "TESOURA": ')).upper()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
sleep(1)
print('\nA escolha do COMPUTADOR foi: {}'.format(computador))
if jogador == 'PEDRA' and computador == emoji.emojize(':oncoming_fist_light_skin_tone:') or jogador == papel and computador == emoji.emojize(':raised_back_of_hand_light_skin_tone:') or jogador == tesoura and computador ==emoji.emojize(':victory_hand_light_skin_tone:'):
    ep = emoji.emojize(':oncoming_fist_light_skin_tone:')
    if jogador == 'PEDRA':
        print('Você escolheu {} e o computador {} que empatam e ninguém ganha!'.format(ep, computador))
    epp = emoji.emojize(':raised_back_of_hand_light_skin_tone:')
    if jogador == 'PAPEL':
        print('Você escolheu {} e o comutador {} que empatam e ninguém ganha!'.format(epp, computador))
    et = emoji.emojize(':victory_hand_light_skin_tone:')
    if jogador == 'TESOURA':
        print('Você escolheu {} e o computador {} que empatam e ninguém ganha!'.format(et, computador))
elif jogador == 'PEDRA' and computador == emoji.emojize(':victory_hand_light_skin_tone:'):
    ep = emoji.emojize(':oncoming_fist_light_skin_tone:')
    if jogador == 'PEDRA':
        print('\nVocê escolheu {} que ganha de {}, PARABÉNS você ganhou!'.format(ep, emoji.emojize(':victory_hand_light_skin_tone:')))
elif jogador == 'PEDRA' and computador == emoji.emojize(':raised_back_of_hand_light_skin_tone:'):
    ep = emoji.emojize(':oncoming_fist_light_skin_tone:')
    if jogador == 'PEDRA':
        print('\nVocê escolheu {} que perde de {}, você perdeu!'.format(ep, emoji.emojize(':raised_back_of_hand_light_skin_tone:')))
elif jogador == 'TESOURA' and computador == emoji.emojize(':oncoming_fist_light_skin_tone:'):
    et = emoji.emojize(':victory_hand_light_skin_tone:')
    if jogador == 'TESOURA':
        print('\nVocê escolheu {} que perde de {}, você perdeu!'.format(et, emoji.emojize(':oncoming_fist_light_skin_tone:')))
elif jogador == 'TESOURA' and computador == emoji.emojize(':raised_back_of_hand_light_skin_tone:'):
    et = emoji.emojize(':victory_hand_light_skin_tone:')
    if jogador == 'TESOURA':
        print('\nVocê escolheu {} que ganha de {}, PARABÉNS você ganhou!'.format(et, emoji.emojize(':raised_back_of_hand_light_skin_tone:')))
elif jogador == 'PAPAEL' and computador == emoji.emojize(':victory_hand_light_skin_tone:'):
    epp = emoji.emojize(':raised_back_of_hand_light_skin_tone:')
    if jogador == 'PAPEL':
        print('\nVocê escolheu {} que perde de {}, você perdeu!'.format(epp, emoji.emojize(':victory_hand_light_skin_tone:')))
elif jogador == 'PAPEL' and computador == emoji.emojize(':oncoming_fist_light_skin_tone:'):
    epp = emoji.emojize(':raised_back_of_hand_light_skin_tone:')
    if jogador == 'PAPEL':
        print('\nVocê escolheu {} que ganha de {}, PARABÉNS você ganhou!'.format(epp, emoji.emojize(':oncoming_fist_light_skin_tone:')))
