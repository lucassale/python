aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'A média do {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprovado'
print('=-='*20)
for k, v in aluno.items():
    print(f'O {k} é igual a {v}...')