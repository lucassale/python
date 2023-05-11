from datetime import date
print('\033[30;42mSAIBA AQUI A HORA DE SE ALISTAR.\033[m')
ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano
if idade == 18:
    print('Chegou o ano do seu alistamento!')
elif idade < 18:
    print('Você ainda irá se alistar. Faltam apenas {} anos!'.format(18 - idade))
else:
    print('Ja se passaram {} anos da data do seu alistamento!'.format(idade - 18))