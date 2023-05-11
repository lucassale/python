print('=-=' * 10, '\033[4;35mCALCULADORA DE IMC\033[m', '=-=' * 10)
a = float(input('Me informe sua altura: '))
p = float(input('Me informe seu peso: '))
imc = p / a ** 2
if imc < 18.5:
    print('Seu IMC é {:.2f}. Você está abaixo do peso.'.format(imc))
elif imc > 18.5 and imc < 25:
    print('Seu IMC é {:.2f}. Parabéns você esta no peso ideal.'.format(imc))
elif imc > 25 and imc < 30:
    print('Seu IMC é {:.2f}. Você está com sobre-peso e precisa de exercícios.'.format(imc))
elif imc > 30 and imc < 40:
    print('Seu IMC é {:.2f}. Você tem obesidade e precisa de ajuda médica especializda.'.format(imc))
elif imc > 40:
    print('Seu IMC é {:.2f}. Você tem obesidade morbida, vá urgente procurar ajuda.'.format(imc))
