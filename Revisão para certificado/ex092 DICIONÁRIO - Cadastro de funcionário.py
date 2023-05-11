from datetime import date
cad = {}
cad['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
cad['idade'] = date.today().year - ano
cad['ctps'] = int(input('Carteira de trabalho (não tem digite 0): '))
if cad['ctps'] != 0:
    cad['contratação'] = int(input('Ano de contratação: '))
    cad['salario'] = float(input('Salário: '))
    cad['aposentadoria'] = (35 - (date.today().year - cad['contratação'])) + cad['idade']
print('=-='*30)
for k, v in cad.items():
    print(f'{k} tem o valor {v}')
print('-'*45)
print(cad)