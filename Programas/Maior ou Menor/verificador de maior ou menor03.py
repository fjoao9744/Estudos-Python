numero = 0
while True:
    numero_antigo = numero
    numero = int(input('Digite um valor: '))

    if numero >= numero_antigo:
        maior = numero
        menor = numero_antigo
    if numero <= numero_antigo:
        maior = numero_antigo
        menor = numero

    continuar = str(input('Deseja continuar?[S/N] ')).strip().upper()
    if continuar == 'N':
        break

print(f'O maior numero digitado foi {maior} e o menor foi {menor}')
