from random import randint
lista = list()
cont = 0
tot = 0
jogos = list()
quant = int(input("Quantos jogos você deseja fazer? "))
while quant > tot:
    while True:
        num = randint(0, 60)
        if num not in lista:
            lista.append(num)
            cont += 1

        if cont >= 6:
            cont = 0
            break
    lista.sort()
    print(f"os numeros sorteados foram: {lista}")
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(jogos)

