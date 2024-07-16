lista = []

for c in range(0, 5):
    n = int(input('digite um numero: '))
    if c == 0:
        lista.append(n)
        print('seu valor foi adicionado na posição 0. ')
    elif n > lista[-1]:
        lista.append(n)
        print(f'seu valor foi adicionado na posição {lista.index(n)}')
    else:
        v = 0
        while v < len(lista):
            if n <= lista[v]:
                lista.insert(v, n)
                break
            v += 1
        print(f'seu valor foi adicionado na posição {lista.index(n)}')



                
            
print(f'sua lista ficou assim: {lista}')
