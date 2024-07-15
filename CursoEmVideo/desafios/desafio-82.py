lista = []
lista_pares = []
lista_impares = []


while True:
    numero = int(input('digite um valor: '))
    lista.append(numero)
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)



    if str(input('Deseja continuar? ')).strip().upper() == 'N':
        break


print(f'sua lista foi {lista} \nos pares da sua lista foram {lista_pares} \ne os impares foram {lista_impares}')