lista = []

while True:
    pessoa = []
    pessoa.append(str(input("Digite o nome do aluno: ")).strip())

    nota1 = int(input("nota1: "))
    nota2 = int(input("nota2: "))
    pessoa.append([nota1, nota2])

    lista.append(pessoa)

    cont = str(input("Deseja continuar?[S/N] ")).strip().upper()

    if cont == "N":
        break

print(lista)

