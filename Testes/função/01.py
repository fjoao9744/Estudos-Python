lista = [' aBc1', 'ABD2', 'ADe3', 'acd4']

def padronizar(x):
    return [x.strip().upper() for x in x]

print(lista)
print(padronizar(lista))

