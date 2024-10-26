lista = []
while True:
    lista.append(int(input('Digite um valor: ')))

    continuar = str(input('Deseja continuar?[S/N] ')).strip().upper()
    if continuar == 'N':
        break

lista.sort()
print(f'O maior numero digitado foi {lista[-1]} e o menor foi {lista[0]}')
