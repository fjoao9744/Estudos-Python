from random import randint
from time import sleep
from operator import itemgetter

jogadores = {
    "jogador1": randint(1, 6),
    "jogador2": randint(1, 6),
    "jogador3": randint(1, 6),
    "jogador4": randint(1, 6)}


print("Valores sorteados: ")

for k, v in jogadores.items():
    sleep(1)
    print(f"O {k} tirou {v}")
    
ranking = sorted(jogadores.items(), key= itemgetter(1), reverse= True) # itemgetter pega varios items de uma tupla ou lista(o .items() retorna uma tupla)

print("=" * 20)
print("== RANKING ==")
for i, p in enumerate(ranking):
    sleep(1)
    print(f"    {i + 1}° Lugar: {p[0]} com {p[1]}")