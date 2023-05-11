def cadastro(n='<desconhecido>', g=0):
    print(f'O jogador {n} fez {g} gols')


nome = str(input('Nome do jogador? '))
gols = str(input('Gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    cadastro(g=gols)
else:
    cadastro(nome, gols)

