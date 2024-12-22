pessoas = []

while True:
    nome = str(input("Digite o nome: ")).strip().capitalize()
    sexo = str(input("Digite o sexo [M/F]: ")).strip().upper()[0]
    idade = int(input("Digite a idade: "))
    
    pessoa = [nome, sexo, idade]
    
    pessoas.append(pessoa)
    
    cont = str(input("Deseja continuar?[S/N] ")).strip().upper()
    
    if cont == "N":
        break

print(pessoas)

print(f"O total de pessoas cadastradas foram de {len(pessoas)} pessoas")
print(f"Com maior idade temos: ", end="")

for pessoa in pessoas:
    if pessoa[2] >= 18:
        print(pessoa[0], end=" ")
print()
        
print(f"Do sexo masculino temos: ", end="")

for pessoa in pessoas:
    if pessoa[1] == "M":
        print(pessoa[0], end=" ")
print()

print(f"Do sexo feminino: ", end="")

for pessoa in pessoas:
    if pessoa[1] == "F":
        print(pessoa[0], end=" ")

''''''

pessoas = []

while True:
    nome = str(input("Digite o nome: ")).strip().capitalize()
    sexo = str(input("Digite o sexo [M/F]: ")).strip().upper()[0]
    idade = int(input("Digite a idade: "))
        
    pessoas.append([nome, sexo, idade])
        
    if str(input("Deseja continuar?[S/N] ")).strip().upper() == "N":
        break

print(f"O total de pessoas cadastradas foram de {len(pessoas)} pessoas")
print(f"Com maior idade temos: ", [pessoa[0] for pessoa in pessoas if pessoa[2] >= 18]) 
        
print(f"Do sexo masculino temos: ", [pessoa[0] for pessoa in pessoas if pessoa[1] == "M"])

print(f"Do sexo feminino: ", [pessoa[0] for pessoa in pessoas if pessoa[1] == "F"])

