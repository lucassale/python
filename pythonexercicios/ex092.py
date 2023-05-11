from datetime import date
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
pessoa['idade'] = date.today().year - ano
pessoa['ctps'] = int(input('Carteira de trabaho (digite 0 se não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['saláro'] = float(input('Sálario: '))
    pessoa['aposentadoria'] = (35 - (date.today().year - pessoa['contratação'])) + pessoa['idade']
print('=-='*30)
for k, v in pessoa.items():
    print(f' - {k} tem o valor {v}')
print(pessoa)