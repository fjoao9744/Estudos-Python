jogadores = []

while True:
    jogador = {}
    jogador["nome"] = str(input("Qual o nome do jogador? ")).strip().capitalize()
    jogador["jogos"] = int(input("Quantas partidas esse jogador jogou? "))


    jogador["gols"] = []

    for _ in range(jogador["jogos"]):
        jogador["gols"].append(int(input(f"Quantos gols foram marcados no jogo {_}? ")))

    jogadores.append(jogador)

    if input("Deseja continuar?[S/N] ").upper().strip()[0] == "N":
        break
    print("-" * 20)


print("-=" * 20)

print(f"{"cod"} {"nome":<20} {"gols":<20} {"total"}")
for i, _ in enumerate(jogadores):
    print(f"{i:>3} {_["nome"]:<20} {_["gols"]} {sum(_["gols"])}")

while True:
    cod = int(input("Mostrar os dados de qual jogador? "))

    if cod == 999:
        break

    if cod >= len(jogadores):
        print("Por favor digite um numero valido")
        continue

    print(f"-- Levantamento do jogador {jogadores[cod]['nome']}:")
    for i, _ in enumerate(jogadores[cod]['gols']):
        print(f"No jogo {i} ele fez {_} gols")

    print("-=" * 10)

print("<< volte sempre >>")

