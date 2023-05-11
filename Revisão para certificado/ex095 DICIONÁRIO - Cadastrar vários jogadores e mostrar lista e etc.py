lista = []
jogadores = {}
gols = []
total = 0
while True:
    jogadores['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
    partidas = int(input(f'Quantas partidas o {jogadores["nome"]} jogou? '))
    for c in range(1, partidas + 1):
        gols.append(int(input(f'Quantos gols na partida {c}? ')))
    jogadores['gols'] = gols[:]
    jogadores['total'] = sum(gols)
    lista.append(jogadores.copy())
    gols.clear()
    resposta = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    while resposta not in 'SN':
        print('Erro! Por favor só responda [S/N].')
        resposta = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if resposta == 'N':
        break
print('=-=' * 45)
print('cod  ', end='')
for k in jogadores.keys():
    print(f'{k:<15}', end='')
print()
print('-'*45)
for i, v in enumerate(lista):
    print(f'{i+1:<4}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*45)
while True:
    j = int(input('Mostrar dados de qual jogador (999 interrompe)? '))
    if j == 999:
        break
    if j > len(lista) or j < 0:
        print('Erro! Esse valor é invalido...')
    else:
        print(f'   LEVANTAMENTO DO JOGADOR {lista[j-1]["nome"]}')
        for i, v in enumerate(lista[j-1]['gols']):
            print(f'     No jogo {i+1} ele fez {v} gols.')