#Camara de teste 2

def banco_dados():
    while True:
        nome = str(input("Digite seu nome: ".strip())).capitalize()
        idade = int(input("Digite sua idade: ".strip()))
        genero = str(input("Digite seu gênero: ").strip()).capitalize()[0]

        pessoas_cadastradas = []

        if genero not in "MF":
            print("Gênero inválido")
            break
        
        else:
            pessoas_cadastradas.append(nome)

        with open("dados.txt", "at") as dados:
            dados.write(f"\n{nome}, {idade} anos, genero: {genero}")

        continuar = str(input("Deseja inserir mais dados?: ")).capitalize().upper()[0]
        
        if continuar in "S":
            continue
        
        else:
            print(f"Foram cadastradas {len(pessoas_cadastradas)} pessoa(s)")
            break


if __name__ == "__main__":
    banco_dados()