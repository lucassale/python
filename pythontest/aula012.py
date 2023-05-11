nome = str(input('Digite seu nome: ')).upper()
if nome == 'LUCAS':
    print('Que nome lindo!')
    print('Muito prazer em te conhecer {}'.format(nome.title()))
elif nome == 'LUNNA':
    print('Esse é um belo nome feminino, PARABÉNS {}!'.format(nome.upper()))
elif nome == 'CARLOS' or nome == 'SALES' or nome == 'ANDRADE':
    print('Seu nome é bem normal.')
else:
    print('Por que não Python!?')
