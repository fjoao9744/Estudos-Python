lista = []
while True:
    n = int(input('digite um numero: '))
    if n in lista:
        print('valor duplicado, não vou adicionar')
    if n not in lista:
        lista.append(n)
        print('adicionado com sucesso...')

    if str(input('Deseja continuar?[S/N] ')).strip().upper() == 'N':
        break

lista.sort()
print(lista)

