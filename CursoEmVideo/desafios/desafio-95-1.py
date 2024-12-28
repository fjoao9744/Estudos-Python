# errado

time = list()
jogador = dict()
partidas = []
while True:
    jogador.clear()
    jogador["nome"] = str(input("Nome do jogador: "))
    tot = int(input(f"Quantas partidas {jogador['nome']} jogou: "))

    for c in range(0, tot):
        partidas.append(int(input(f"Quanto gols o {jogador['nome']} fez na partida {c}: ")))

    print(jogador)
    print("-=" * 20)
    
    jogador['gols'] = partidas[:]
    jogador["total"] = sum(partidas)
    
    time.append(jogador.copy())
    
    while True:
        resp = str(input("Quer continuar?[S/N] ")).upper()[0]
        if resp in "SN":
            break
        print("Erro, digite apenas S ou N")
        
    if resp == "N":
        break

for k, v in enumerate(time):
    print(f"{k:>3}", end=' ')
    for d in v.values():
        print(f"{str(d):<15}")
    print()

