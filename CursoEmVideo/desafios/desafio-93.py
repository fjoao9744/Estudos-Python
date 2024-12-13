jogador = {}

jogador["nome"] = str(input("Qual o nome do jogador? ")).strip().capitalize()
jogador["jogos"] = int(input("Quantas partidas esse jogador jogou? "))

jogador["gols"] = []

for _ in range(jogador["jogos"]):
    jogador["gols"].append(int(input(f"Quantos gols foram marcados no jogo {_ + 1}? ")))

print("-=" * 20)
print(jogador)
print("-=" * 20)

print(f"O jogador tem o nome de {jogador['nome']}")
print(f"Seus gols tem o valor de {jogador['gols']}")
print(f"O jogador tem no total {sum(jogador['gols'])} de gols")
print("-=" * 20)
print(f"O jogador {jogador['nome']} jogou {jogador['jogos']} jogos.")
for i, _ in enumerate(jogador['gols']):
    print(f"     => Na partida {i + 1}, fez {_} gols.")
print(f"Fez um total de {sum(jogador['gols'])}")