sexo = str(input('Digite seu sexo [M/F]: ')).upper()[0].strip()
while sexo not in 'MF':
    sexo = str(input('Dado inválido, por favor digite seu sexo: ')).upper()[0].strip()
if sexo == 'M':
    print('Seu sexo é MASCULINO.')
else:
    print('Seu sexo é FEMINIO')