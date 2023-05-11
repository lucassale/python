tabela = 'Palmeiras', 'Corinthians', 'Fluminense', 'Alético-MG', 'Athletico-PR', 'Flamengo', 'Internacional', 'Bragantino', 'Santos', 'São Paulo', 'Botafogo', 'Ceará SC', 'Coritiba',  'Goiás', 'Ámerica-MG', 'Avaí', 'Cuiabá', 'Atlético-GO', 'Juventude', 'Fortaleza'
print(f'A lista de times do Brasileirão: \033[1;34m{tabela}\033[m')
print(f'Os 5 primeiros são: \033[1;32m{tabela[:5]}\033[m')
print(f'Os 4 últimos são: \033[1;31m{tabela[16:]}\033[m')
print(f'Os times em Ordem Alfabética: \033[1;33m{sorted(tabela)}\033[m')
print(f'\033[1;35mO Flamengo está na {tabela.index("Flamengo")+1}° posição.\033[m')