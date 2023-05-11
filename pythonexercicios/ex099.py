def maior(* n):
    from time import sleep
    m = c = 0
    print('Analisando os valores passados')
    for i, v in enumerate(n):
        if i == 0:
            m = v
        else:
            if v > m:
                m = v
        print(v, end=' ')
        c += 1
        sleep(0.5)
    print(f'Foram informados {c} valores.')
    print(f'O maior valor entre {n} é {m}.')
    print('=-='*20)


maior(1, 2, 3, 41, 5, 6)
maior(7, 105, 44, 3, 88)
maior(-4, -8, 10, -1)
maior(1)
maior()