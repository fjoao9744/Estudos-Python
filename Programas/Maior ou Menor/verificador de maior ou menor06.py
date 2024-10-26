lista = []

começo = int(input('quantos numeros deseja verificar? '))
for contador in range(1, começo + 1):
    lista.append(int(input(f'digite o {contador}° valor: ')))

print(f'O maior valor digitado foi {max(lista)} e o menor foi {min(lista)}')