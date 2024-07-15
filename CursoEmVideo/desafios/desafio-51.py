print('='*10 ,'10 TERMOS DE P.A', '='*10)
print('='*40)

n1 = int(input('digite o primeiro termo: '))
n2 = int(input('digite a razâo: '))
dec = n1 + (10-1) * n2

for c in range(n1, dec + n2, n2):
    print(c, end=' ')


