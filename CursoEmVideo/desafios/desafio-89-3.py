lista = []

while True:
    pessoa = []
    nome = str(input("Nome: ")).strip()
    pessoa.append(nome)

    notas = []
    notas.append(float(input("nota 1: ")))
    notas.append(float(input("nota 2: ")))
    pessoa.append(notas)

    lista.append(pessoa)

    cont = str(input("Deseja continuar?[S/N] ")).strip().upper()

    if cont == "N":
        break
print("-=" * 20)
print(f"{"No.":<4}{"Nome":<10}{"Media":>8}")
print("-" * 20)

for i, c in enumerate(lista):
    print(f"{i:<4}{c[0]:<10}{(c[1][0] + c[1][1]) // 2:>8}")

while True:
    aluno = int(input("Você deseja ver as notas de qual aluno?[999 para parar] "))
    if aluno == 999:
        break
    
    if aluno > len(lista) - 1:
        print("Digite um numero valido")
        continue


    print(f"As notas de {lista[aluno][0]} foram {lista[aluno][1]}")

