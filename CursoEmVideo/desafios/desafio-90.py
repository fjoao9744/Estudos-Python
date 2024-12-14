alunos = []

while True:
    aluno = {}
    aluno["nome"] = str(input("Nome: ")).strip().capitalize()
    aluno["media"] = float(input(f"Média de {aluno['nome']}: "))
    if aluno["media"] >= 7:
        aluno["situação"] = "aprovado"
    else:
        aluno["situação"] = "reprovado"

    alunos.append(aluno)

    cont = str(input("Deseja continuar? [S/N] ")).strip().upper()

    if cont == "N":
        break

for _ in alunos:
    print(f"A média de {_['nome']} foi {_['media']} e ele esta {_['situação']}")