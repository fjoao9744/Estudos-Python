lista = []

menor = maior = 0
for c in range(0, 5):
    lista.append(int(input(f'digite um valor na posição {c}: ')))
    if c == 0:
        menor = maior = lista[c]
    else:
        if lista[c] >= maior:
            maior = lista[c]
        if lista[c] <= menor:
            menor = lista[c]    

print(f'você digitou {lista}')
print(f'o maior valor foi {maior} na posição: ', end='')
for c, i in enumerate(lista):
    if i == maior:
        print(f'{c}...', end='')
print(f'\no menor valor foi {menor} na posição: ', end='')
for c, i in enumerate(lista):
    if i == menor:
        print(f'{c}...', end='')

    