print('Preciso de três retas para formar um triângulo.')
r1 = int(input('Digite quanto mede a primeira reta: '))
r2 = int(input('Digite a segunda reta: '))
r3 = int(input('Digite a terceira reta: '))
if (r1 + r2) > r3:
    print('Parabéns, essas retas formam um triângulo!')
else:
    print('Que pena essas retas não formam um triângulo.')
