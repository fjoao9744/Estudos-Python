lista = []

menor = maior = 0
for c in range(0, 5):
    lista.append(int(input(f'digite um valor na posição {c}: ')))
    
maior, menor = max(lista), min(lista)


print(f'você digitou {lista}')
print(f'o maior valor foi {maior} na posição: ', end='')
n = 0
lista_copia1 = lista[:]

while maior in lista_copia1:
    print(lista_copia1.index(maior) + n, end='...')
    lista_copia1.remove(maior)
    n += 1
lista_copia2 = lista[:]
n = 0
print(f'\no menor valor foi {menor} na posição: ', end='')
while menor in lista_copia2:
    print(lista_copia2.index(menor) + n, end='...')
    lista_copia2.remove(menor)
    n += 1

    