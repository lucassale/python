lista = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    média = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], média])
    res = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    while res not in 'SN':
        res = str(input('Resposta inválida... Quer continur [S/N]? ')).strip().upper()[0]
    if res == 'N':
        break
print('=-='*30)
print(f'{"N°":<4}{"Nome":<8}{"Média":>4}')
for i, a in enumerate(lista):
    print(f'{i+1:<4}{a[0]:<8}{a[2]:>4.1f}')
while True:
    print('-' * 45)
    a = int(input('De qual aluno deseja ver as notas (Digite 999 para parar)? '))
    if a > len(lista):
        print('\033[1;31mNão temos esse número cadastrado! Tente outro\033[m')
    else:
        print(f'As notas de {lista[a-1][0]} são: {lista[a-1][1]}')
    if a == 999:
        break
print('Programa finalizado...')
