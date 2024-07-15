#errado

lista = []

menor = maior = 0
for c, v in enumerate(range(0, 5)):
    lista.append(int(input(f'digite um valor na posição {c}: ')))
    
    
maior, menor = max(lista), min(lista)


print(f'você digitou {lista}')
print(f'o maior valor foi {maior} na posição: ')
n = 0
for c in lista :
    if c == maior:
        print(lista.index(maior) + n)
        lista.remove(c)
        n += 1
        


print(f'\no menor valor foi {menor} na posição:')
