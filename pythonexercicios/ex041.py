from datetime import date
print('=*=' * 10, '\033[1;34mSELEÇÃO DE CATEGORIAS PARA NATAÇÃO\033[m', '=*=' * 10)
ano = int(input('Digite aqui seu ano de nascimento: '))
idade1 = date.today().year - ano
idade2 = ano - date.today().year
if idade1 <= 9:
    print('Você será da categoria Mirin!')
elif idade1 <= 14:
    print('Você será da categoria Infantil!')
elif idade1 <= 19:
    print('Você será da categoria Junior!')
elif idade1 <=20:
    print('Você será da categoria Sênior!')
elif idade1 > 20:
    print('Você será da categoria Master!')