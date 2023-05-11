def ficha(nome, gols):
    if nome.strip() == '':
        nome = '<desconhecido>'
    if gols.isnumeric():
        gols = int(gols)
    elif gols == '':
        gols = 0
    print(f'O jogador {nome} fez {gols} gols.')


nome = str(input('Nome do jogador: '))
gols = str(input('Gols do jogador: '))
print('=-='*20)
ficha(nome, gols)
