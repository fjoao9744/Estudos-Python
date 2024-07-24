lista = []
par = []
impar = []

for c in range(0, 7):
    n = int(input(f'digite o {c + 1}° numero: '))
    
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

par.sort()
impar.sort()

print(f'os valores pares digitados foram: {par}')
print(f'os vlaores impares digitados foram: {impar} ')
