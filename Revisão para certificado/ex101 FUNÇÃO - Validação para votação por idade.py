def voto(n=0):
    from datetime import date
    idade = date.today().year - n
    if idade >= 18 and idade < 65:
        return (f'Com {idade} anos: VOTO OBRIGATÓRIO!')
    if idade < 18:
        return (f'Com {idade} anos: VOTO NEGADO!')
    if idade >= 65:
        return (f'Com {idade} anos: VOTO OPICIONAL!')


n1 = int(input('Qual sua data de nasciment? '))
print(voto(n1))