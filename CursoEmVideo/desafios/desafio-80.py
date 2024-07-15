#errrado

lista = []
lista1 = []
for c in range(0, 5):
    n = int(input('digite um numero: '))
    lista1.append(n)
    for c in lista1:
        if n <= c:
            lista.insert(lista1.index(c), c)



                
            


             
    print(lista, lista1)
