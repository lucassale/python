v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
v3 = int(input('Digite o terceiro valor: '))
menor = v1
maior = v1
if v2 < v1 and v2 < v3:
    menor = v2
if v3 < v1 and v3 < v2:
    menor = v3
if v2 > v1 and v2 > v3:
    maior = v2
if v3 > v1 and v3 > v2:
    maior = v3

print('Entre os números {}, {} e {} o maior é: {}'.format(v1, v2, v3, maior))
print('Entre os números {}, {} e {} o menor é: {}'.format(v1, v2, v3, menor))
