def ficha(nome="<desconhecido>", gols=0):
    print(f"o jogador {nome} fez {gols} gols")
    
nome = str(input("Digite o nome do jogador: ")).strip()
gols = str(input("Quantos gols o jogador fez: "))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome.strip() == '':
    ficha(gols=gols)
else:
    ficha(nome, gols)