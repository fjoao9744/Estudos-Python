aluno = dict()

aluno["nome"] = str(input("Nome: ")).strip().capitalize()
aluno["media"] = float(input(f"Média de {aluno['nome']}: "))

if aluno["media"] >= 7:
    aluno["situação"] = "aprovado"

elif 5 <= aluno["media"] < 7: # se a media for maior que 5 e menor que 7(media > 5 and media < 7)
    aluno["situação"] = "recuperação"

else:
    aluno["situação"] = "reprovado"

print(aluno)
print("-=" * 30)
for k, v in aluno.items():
    print(f"  - {k} é igual a {v}")

