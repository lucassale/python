jogador = {}
jogador['nome'] = str(input('Nome: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
gols = []
total = 0
for p in range(1, partidas + 1):
    gols.append(int(input(f'{"":>5}Quantos gols na partida {p}? ')))
for g in gols:
    total += g
jogador['gols'] = gols[:]
jogador['total'] = total
#jogador['total'] = sum(total) sem precisar do for dos gols!
print('=-='*30)
print(jogador)
print('=-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=-='*30)
print(f'O jogador {jogador["nome"]} jogou {partidas}.')
for i, g in enumerate(gols):
    print(f'{"=>":>5}Na partida {i} ele fez {g} gols.')
print(f'Foi um total de {total} gols.')
