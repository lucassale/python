def notas(*n, situação=False):
    l = {}
    l['total'] = len(n)
    l['maior'] = max(n)
    l['menor'] = min(n)
    l['média'] = sum(n) / len(n)
    if situação:
        if l['média'] > 7:
            l['situação'] = 'BOA'
        elif l['média'] == 7:
            l['situação'] = 'RAZOÁVEL'
        else:
            l['situação'] = 'RUIM'
    return l


dados = notas(7.5, 4, 9.5, situação=True)
print(dados)