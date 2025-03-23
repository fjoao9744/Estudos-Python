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

def resumo(num, p1, p2):
    print("-" * 30)
    print(f"{'RESUMO DO VALOR':^30}")
    print("-" * 30)
    
    print(f"Preço analisado: {f"R${num:.2f}".replace(".", ","):>10}")
    print(f"Dobro do valor: {dobro(num, True):>10}")
    print(f"Metade do preço: {metade(num, True):>10}")
    print(f"{p1}% de aumento: {aumentar(num, p1, True):>10}")
    print(f"{p2}% de redução: {diminuir(num, p2, True):>10}")
    
    print("-" * 30)
    
    