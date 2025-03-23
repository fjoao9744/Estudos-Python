def aumentar(num, p, form=False):
    n = num + ((num * p) // 100)
    
    if not form:
        return n
    
    return f"R${n:.2f}".replace(".", ",")
    
def diminuir(num, p, form=False):
    n = num - ((num * p) // 100)
    
    if not form:
        return n
    
    return f"R${n:.2f}".replace(".", ",")
    
def metade(num, form=False):
    n = num // 2
    if not form:
        return n
    
    return f"R${n:.2f}".replace(".", ",")
    
def dobro(num, form=False):
    n = num * 2
    if not form:
        return num * 2
    
    return f"R${n:.2f}".replace(".", ",")
