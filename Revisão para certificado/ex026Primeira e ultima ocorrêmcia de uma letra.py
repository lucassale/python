frase = str(input('Digite um frase: ')).lower().strip()
#a = frase.count('a')
print('A letra "A" aparece {} vezes.'.format(frase.count('a')))
print('A letra "A" aparece primeiro na posição {}'.format(frase.find('a') + 1))
print('A letra "A" aparece pela última vez na posição {}'.format(frase.rfind('a') + 1))
