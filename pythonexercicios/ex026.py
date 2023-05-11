frase = str(input('Digite uma frase: ')).strip().lower()
print('Nessa frase a letra "A" se repete {} vezes'.format(frase.count('a')))
print('A posição da primeira letra "A" é {}'.format(frase.find('a')+1))
print('A última posição da letra "A" é {}'.format(frase.rfind('a')+1))
#ERRO NO CASO DE ACENTUÇÃO#