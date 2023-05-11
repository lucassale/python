jogador = {}
jogador['nome'] = str(input('Nome do jogador: '))
q = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
gols = []
for c in range(1, q+1):
    gols.append(int(input(f'Quantos gols na partida {c}: ')))
jogador['gols'] = gols
jogador['total'] = sum(gols)
print('=-='*30)
print(jogador)
print('=-='*30)
for k, v in jogador.items():
    print(f'O compo {k} tem o valor {v}')
print('=-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(gols)} partidas.')
for g in range(1, len(gols)+1):
    print(f'   => Na partida {g}, fez {gols[g-1]}.')
