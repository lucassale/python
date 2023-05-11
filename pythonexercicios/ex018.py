from math import cos, sin, tan, radians
ang = float(input('Qual o ângulo? '))
c = cos(radians(ang))
s = sin(radians(ang))
t = tan(radians(ang))
print('o coseno, seno e tangente de {} graus é respectivamento: {:.2f}, {:.2f} e {:.2f}'.format(ang, c, s, t))
