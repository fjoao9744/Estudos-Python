lista = []
cont = 0
while True:
    numero = int(input('digite um numero: '))
    lista.append(numero)
    cont += 1

    if str(input('Deseja continuar?[S/N] ')).strip().upper() == 'N':
        break

print(f'você digitou {cont} numeros')
lista.sort(reverse=True)
print(f'a ordem deles descente é {lista}')
print('e o valor 5 foi digitado' if 5 in lista else 'o valor 5 não foi digitado')

