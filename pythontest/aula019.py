estado = {}
brasil = []
for c in range(0, 3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['SIGLA'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)
print()
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
