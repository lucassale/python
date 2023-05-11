j = {}
time = []
gols = []
while True:
    total = 0
    j.clear()
    gols.clear()
    j['nome'] = str(input('Nome do jogador: '))
    p = int(input(f'Quantas partidas o {j["nome"]} jogou? '))
    for g in range(1, p+1):
        gols.append(int(input(f'Quantos gols na {g}° partida? ')))
    j['gols'] = gols[:]
    j['total'] = sum(gols)
    time.append(j.copy())
    r = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('ERRO! Só responta [S/N]. Quer continuar [S/N]? ')).strip().upper()[0]
    if r =='N':
        break
print('=-='*30)
print('cod ', end='')
for k in j.keys():
    print(f'{k:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:<3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('=-='*30)
while True:
    e = int(input('Mostar os dados de qual jogador? (999 interrompe: '))
    if e == 999:
        break
    if e >= len(time):
        print(f'ERRO! Não existe jogador com o código {e}!')
    else:
        print(f'--LEVANTAMENTO DO JOGADOR {time[e]["nome"]}')
        for i, g in enumerate(time[e]['gols']):
            print(f'   No jogo {i+1} ele fez {g} gols.')
    print('-'*40)
print('<<<VOLTE SEMPRE>>>')