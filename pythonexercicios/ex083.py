exp = str(input('Digite uma expressão: '))
p = []
for simb in exp:
    if simb == '(':
        p.append('(')
    elif simb == ')':
        if len(p) > 0:
            p.pop()
        else:
            p.append(')')
            break
print('=-='*30)
if len(p) == 0:
    print('A expressão é válida!')
else:
    print('A expressão é inválida!')