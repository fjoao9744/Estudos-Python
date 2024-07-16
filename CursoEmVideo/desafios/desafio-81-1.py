lista = []
while True:
    numero = int(input('digite um numero: '))
    lista.append(numero)

    if str(input('Deseja continuar?[S/N] ')).strip().upper() == 'N':
        break

print(f'a lista é {lista}')
print(f'você digitou {len(lista)} numeros')
lista2 = lista[:]
lista2.sort(reverse=True)
print(f'a ordem deles descente é {lista2}')
print('o numero 5...', end='')
if 5 in lista:
    print(' aparece na lista na posição: ', end='')
    n = 0
    for c in lista:
        if c == 5:
            print(lista.index(5) + n, end=' ')
            lista.remove(5)
            n += 1

else:
    print('não aparece na lista')

