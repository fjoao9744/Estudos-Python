lista = []
lista_pares = []
lista_impares = []


while True:
    lista.append(int(input('digite um valor: ')))
    if str(input('Deseja continuar? ')).strip().upper() == 'N':
        break

for c in lista:
    if c % 2 == 0:
        lista_pares.append(c)
    else:
        lista_impares.append(c)
print(f'sua lista foi {lista} \nos pares da sua lista foram {lista_pares} \ne os impares foram {lista_impares}')

