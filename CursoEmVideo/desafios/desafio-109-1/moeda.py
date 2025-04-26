def aumentar(num, p, form=False):
    n = num + ((num * p) // 100)
    
    return n if not form else f"R${n:.2f}".replace(".", ",")
        
def diminuir(num, p, form=False):
    n = num - ((num * p) // 100)
    
    return n if not form else f"R${n:.2f}".replace(".", ",")

    
def metade(num, form=False):
    n = num // 2
    
    return n if not form else f"R${n:.2f}".replace(".", ",")

    
def dobro(num, form=False):
    n = num * 2
    
    return n if not form else f"R${n:.2f}".replace(".", ",")
