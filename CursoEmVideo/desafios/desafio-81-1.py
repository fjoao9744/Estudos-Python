#errado
lista = []
cont = 0
while True:
    numero = int(input('digite um numero: '))
    lista.append(numero)
    cont += 1

    if str(input('Deseja continuar?[S/N] ')).strip().upper() == 'N':
        break

print(f'a lista é {lista}')
print(f'você digitou {cont} numeros')
lista2 = lista[:]
lista2.sort(reverse=True)
print(f'a ordem deles descente é {lista2}')
print('a numero 5...', end='')
if 5 in lista:
    print(' aparece na lista na posição: ', end='')
    for c in lista:
        if c == 5:
            print(lista.index(5))    
else:
    print('não aparece na lista')