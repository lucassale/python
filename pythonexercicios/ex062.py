print('GERADOR DE PA')
primeiro = int(input('Digito o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        contador += 1
    print('PAUSA')
    mais = int(input('Quer ver mais quantos termos? '))
print('A PA finalizou com {} termos.'.format(total))
