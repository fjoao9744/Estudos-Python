def aumentar(num, p):
    return num + ((num * p) // 100)
    
def diminuir(num, p):
    return num - ((num * p) // 100)
    
def metade(num):
    return num // 2
    
def dobro(num):
    return num * 2

def moeda(num):
    return f"R${num:.2f}".replace(".", ",")