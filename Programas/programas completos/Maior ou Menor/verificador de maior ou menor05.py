lista = []
while True:
    lista.append(int(input('Digite um valor: ')))

    continuar = str(input('Deseja continuar?[S/N] ')).strip().upper()
    if continuar == 'N':
        break

print(f'O maior numero digitado foi {max(lista)} e o menor foi {min(lista)}')
