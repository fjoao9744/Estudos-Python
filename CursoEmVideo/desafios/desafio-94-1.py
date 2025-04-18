pessoas = []

while True:
    pessoa = {}
    pessoa["nome"] = str(input("Nome: ")).strip().capitalize()
    pessoa["sexo"] = str(input("Sexo[F/M]: ")).strip().upper()
    while pessoa["sexo"] not in "FM":
        print("Por favor, digie um sexo valido")
        pessoa["sexo"] = str(input("Sexo[F/M]: ")).strip().upper()
        
    pessoa["idade"] = int(input("idade: "))

    pessoas.append(pessoa)

    cont = str(input("Deseja continuar? [S/N] ")).strip().upper()
    while cont not in "SN":
        print("Por favor, digite apenas S ou N")
        cont = str(input("Deseja continuar? [S/N] ")).strip().upper()

    if cont[0] == "N":
        break

print(f"Ao todo foram cadastradas {len(pessoas)} pessoas")

media_idade = int()

for _ in pessoas:
    media_idade += _["idade"]

media_idade /= len(pessoas)

print(f"A media de idade entre os cadastrados é de {media_idade:.2f}")

print("Todas as mulheres cadastradas foram:", end=" ")
for _ in pessoas:
    if _["sexo"][0] == "F":
        print(_["nome"], end=" ")
print()

print("E todas as pessoas com a idade acima foram:")
for _ in pessoas:
    if _["idade"] >= media_idade:
        print("     =>", _["nome"], _["sexo"], _["idade"])


