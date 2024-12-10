# errado

from random import randint

jogadores = []

for c in range(4):
    jogador = {}
    jogador["nome"] = str(input("nome:"))
    jogador["num"] = randint(1, 10)
    print(f"O numero que caiu para {jogador['nome']} foi {jogador['num']}")

    jogadores.append(jogador)

maior = 0

for i, _ in enumerate(jogadores):
    if i == 0:
        maior = _
        

    if _["num"] > maior['num']:
        maior = _

print(jogadores)
print(f"O maior numero da lista de jogadores é {maior['num']} do {maior['nome']}")
