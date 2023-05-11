def maior(* v):
    from time import sleep
    m = cont = 0
    print('=-='*30)
    print('Analisando os valores passados...')
    for n in v:
        print(f'{n}', end=' ')
        sleep(0.5)
        if cont == 0:
            m = n
        else:
            if n > m:
                m = n
        cont += 1
    print(f'Foram informados {len(v)} valores ao todo.')
    print(f'O maior valor digitado foi {m}.')


maior(1, 2, 3, 9, 8, 7)
maior(4, 5, 9, 7, 8, 1, 0, 11)
maior(0,0,0,0,0,0)
maior(-7, -2, -9,)
maior()
