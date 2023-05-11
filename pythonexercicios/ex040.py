print('VAMOS VER SE VOCÊ FOI APROVADO...')
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('Sua média é \033[1;31m{:.2f}\033[m, portanto você está \033[1;31mREPROVADO!\033[m'.format(media))
elif media > 7:
    print('Sua média é \033[1;32m{:.2f}\033[m, portanto você está \033[1;32mAPROVADO!\033[m'.format(media))
elif media >= 5 or media < 6.9:
    print('Sua nota é \033[1;33m{:.2f}\033[m, portanto você está de \033[1;33mRECUPERAÇÃO!\033[m'.format(media))
