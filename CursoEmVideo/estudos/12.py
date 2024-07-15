count = int(input('quantos numeros você vai querer contar?'))
count2 = 0
lista = aux = list()
soma = 0

'''for c in range(0 , count):
    aux = int(input('digite o numero: '))

    if aux != 0:
        lista.append(aux)
        soma += aux
    else:
        lista.pop()

    print(lista)

print('a soma de todos os valores foi de {}'.format(soma))
'''
while count2 != count:
    
    aux = int(input('digite o numero: '))
    if aux != 0:
        lista.append(aux)
        count2 += 1
    else:
        lista.pop()
        
    print(lista)
for c in lista[0:]:
    soma += c
print('a soma de todos os valores foi de {}'.format(soma))


