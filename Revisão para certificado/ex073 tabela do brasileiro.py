tabela = ('Palmeiras', 'Fluminense', 'Internacional', 'Corintians', 'Flamengo', 'Atletico-PR', 'Atletico-MG',
          'America-MG', 'Botafogo', 'Santos', 'Goias', 'São Paulo', 'Bragantino', 'Fortaleza', 'Curitiba',
          'Ceara', 'Cuiaba', 'Avai', 'Atletico-GO', 'Juventude')
print(f'Os 5 primeiros colocados são: {tabela[0:5]}')
print(f'Os últimos 4 colocados são: {tabela[-4:]}')
print(sorted(tabela))
print(f'O time do Flamengo esta na {tabela.index("Flamengo") + 1}° posição.')