def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1

l = [1, 3, 5, 6, 10, 20]
print(l)
dobra(l)
print(l)

def aumentar(num):
    num += 1
    
n = 1
print(n)
aumentar(n)
print(n)
    
