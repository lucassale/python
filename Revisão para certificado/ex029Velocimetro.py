velo = int(input('Em que velocidade você estava? '))
exc = (velo - 80)
multa = (exc * 7)
if velo > 80:
    print('Você passou {}km além do permitido. Portanto será multado...'.format(exc))
    print('Sua multa será de R$7.0 para cada km ultrapassado...')
    print('===CALCULANDO===')
    print('MULTA: R${:.2f}'.format(multa))
else:
    print('PARABENS! CONTINUE RESPEITANDO A LEIS DE TRÂNSITO.')
