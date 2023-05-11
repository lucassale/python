from time import sleep
velocidade = float(input('Em que velocidade você passou no radar? '))
radar = float(velocidade - 60)
print('Você passou {}km acima do permitido.'.format(radar))
taxa = float(7)
if velocidade >60:
    print('Você será multado em {}R$ por cada km ultrapassado.'.format(taxa))
    print('CALCULANDO MULTA...')
    sleep(5)
    print(taxa * radar)
else:
    print('Muito bem! Continue respeitando as sinalizações.')