pessoa = {}
pessoa['Nome'] = str(input('Nome: '))
pessoa['Média'] = float(input('Média: '))
print(f'A situação de {pessoa["Nome"]} é: ', end='')
if pessoa['Média'] >= 7:
    print('Aprovada!')
else:
    print('Reprovada!')