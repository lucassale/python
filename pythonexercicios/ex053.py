frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
'''inverso = junto[::-1]'''
for c in range(len(junto) -1, -1, -1):
    inverso += junto[c]
print('O inverso de {} é {}'.format(junto, inverso))
if junto == inverso:
    print('É um palindromo!')
else:
    print('Não é um palindromo!')
