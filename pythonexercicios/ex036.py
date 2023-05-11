from time import sleep
print('=R$=' * 5, '\033[0;32mEMPRESA EMPRESTUSIM EMPRESTIMOS\033[m', '=R$=' * 5)
print('Aprovamos seu empréstimo 5 segundos.')
casa = float(input('Digite o valor do imóvel que pretende comprar: '))
salario = float(input('Digite seu salário: '))
ano = int(input('Em quantos anos quer pagar: '))
parcelas = casa / (ano * 12)
print('=' * 5, 'CALCULANDO', '=' * 5)
sleep(5)
if parcelas > (salario * 30) / 100:
    print('Como o valor das parcelas ultrapassa 30% do seu salário, não poderemos aprovar.')
    print('RESUMO:')
    print('Seu empréstimo é de \033[;35m${:.2f}\033[m\nE as parcelas ficarão divididas em {} parcelas de R${:.2f}.'.format(casa, (ano * 12), parcelas))
else:
    print('PARABENS! Seu empréstimo foi aprovado. Abaixo verá o resumo:')
    print('Seu empréstimo é de \033[;33mR${:.2f}\033[m\nE as parcelas ficarão divididas em {} parcelas de R${:.2f}.'.format(casa, (ano * 12), parcelas))
