ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    média = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], média])
    r = str(input('Quer continuar [S/N]? '))
    if r in 'Nn':
        break
print('=-='*30)
print(f'{"N°":<4}{"Nome":<10}{"Média":<3}')
print('-'*30)
for i, a in enumerate(ficha):
    print(f'{i+1:<4}{a[0]:<10}{a[2]:<3}')
print('=-='*30)
while True:
    print('-'*30)
    ver = int(input('Quer ver a nota de qual aluno? (999 interrompe): '))
    if ver == 999:
        print('FINALIZANDO...')
        break
    if ver <= len(ficha) - 1:
        print(f'As notas de {ficha[ver][0]} são {ficha[ver][1]}.')
print('<<< VOLTE SEMPRE >>>')
