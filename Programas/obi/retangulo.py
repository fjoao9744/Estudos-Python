#errado

n = int(input())
arvores = list(map(int, input().split()))
lado = sum(arvores) // 4

aux = 0

for c in arvores:
    print(arvores, aux)
    aux += c
    arvores.pop(0)
    
    if aux == lado:
        aux = 0
    
    

