jogador = dict()
partidas = []

jogador["nome"] = str(input("Nome do jogador: "))
tot = int(input(f"Quantas partidas {jogador['nome']} jogou: "))

for c in range(0, tot):
    partidas.append(int(input(f"Quanto gols o {jogador['nome']} fez na partida {c}: ")))

print(jogador)
print("-=" * 20)

jogador['gols'] = partidas[:]
jogador["total"] = sum(partidas)
for k, v in jogador.items():
    print(f"O campo {k} tem o valor {v}")

print("-=" * 20)

print(f"O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas.")
for i, v in enumerate(jogador['gols']):
    print(f"    -> na partida {i} fez {v} gols")
    
print(f"O jogador fez {jogador['total']} gols")