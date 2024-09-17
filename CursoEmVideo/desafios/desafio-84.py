#faça um programa que leia o nome e o peso de varias pessoas e mostre a mais leve a mais pesada

pessoas = []
mais_pesados = []
mais_leves = []
while True:
    aux = []
    aux.append(str(input("Nome: ")).strip())
    aux.append(float(input("Peso: ")))
    pessoas.append(aux)


    cont = str(input('Deseja continuar?[S/N] ')).strip().upper()
    if cont == 'N':
        break

maior = menor = pessoas[0][1]

for _ in pessoas:
    if _[1] >= maior:
        maior = _[1]
    if _[1] <= menor:
        menor = _[1]

for _ in pessoas:
    if _[1] == maior:
        mais_pesados.append(_[0])
    if _[1] == menor:
        mais_leves.append(_[0])

print(f"Você cadastrou {len(pessoas)} pessoas")
print(f"O maior peso registrado foi de {maior}Kg. peso de {mais_pesados}")
print(f"O menor peso registrado foi de {menor}Kg. peso de {mais_leves} ")


