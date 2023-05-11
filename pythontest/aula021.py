'''#help(input)
#print(print.__doc__)

def teste(b):
    global a# Usando o GLOBAL o escopo da variável a vale tanto dentro da função como no programa principal(escopo global)!
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}.')
    print(f'B dentro vale {b}.')
    print(f'C dentro vale {c}.')



a = 5
teste(a)
print(f'A fora vale {a}.')


print('=-='*10)
print('=-='*10)



def somar(a=0, b=0, c=0):
    soma = a + b + c
    return soma


r1 = somar(1, 2, 3)
r2 = somar(4, 5)
r3 = somar(6)
print(f'Os resultados das soma foram: {r1}, {r2} e {r3}')'''


def fatorial(n=1):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
f1 = fatorial(3)
f2 = fatorial(10)
print(f'O fatorial de {n} é igual a {fatorial(n)}')
print(f'Os resultados são {f1} e {f2}')