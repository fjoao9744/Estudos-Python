s = int(input()) # soma que tem que dar
a = int(input()) # primeiro numero
b = int(input()) # ultimo numero



def soma_digitos(x):
    lista = sum(int(n) for n in str(x))

    return lista

cont = 0
for c in range(a, b + 1):
    soma = soma_digitos(c)
    if soma == s:
        cont += 1

print(cont)


