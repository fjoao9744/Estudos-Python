matriz = [[0,0,0],[0,0,0],[0,0,0]]
spar = scol = mai = 0

for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f"Digite um valor para: {l,c}"))
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]

for l in range(3):
    for c in range(3):
        print(f"{matriz[l][c]:^5}", end=' ')
    print()
    
print(spar)

for l in range(3):
    scol += matriz[l][2]

print(scol)

for c in range(3):
    if c == 0:
        mai = matriz[1][c]
    if matriz[1][c] > mai:
        mai = matriz[1][c]

print(mai)
