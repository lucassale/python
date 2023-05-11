from math import sin, cos, tan, radians
a = int(input('Digite um ângulo: '))
seno = sin(radians(a))
print('O seno de {}° graus é {:.2f}'.format(a, seno))
cosseno = cos(radians(a))
print('O coseno de {}° graus é {:.2f}'.format(a, cosseno))
tangente = tan(radians(a))
print('A tangente de {}° graus é {:.2f}'.format(a, tangente))
