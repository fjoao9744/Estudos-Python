def aumentar(num = 0, p = 0):
    return num + ((num * p) // 100)
    
def diminuir(num = 0, p = 0):
    return num - ((num * p) // 100)
    
def metade(num = 0):
    return num // 2
    
def dobro(num = 0):
    return num * 2

def moeda(num = 0, moeda = "R$"):
    return f"{moeda}{num:>8.2f}".replace(".", ",")