def aumentar(num, p, form=False):
    n = num + ((num * p) / 100)
    
    return n if not form else f"R${n:.2f}".replace(".", ",")
        
def diminuir(num, p, form=False):
    n = num - (num * p / 100)
    
    return n if not form else f"R${n:.2f}".replace(".", ",")

    
def metade(num, form=False):
    n = num / 2
    
    return n if not form else f"R${n:.2f}".replace(".", ",")

    
def dobro(num, form=False):
    n = num * 2
    
    return n if not form else f"R${n:.2f}".replace(".", ",")

def resumo(num, p1, p2):
    print("-" * 30)
    print(f"{'RESUMO DO VALOR':^30}")
    print("-" * 30)
    
    print(f"Preço analisado: \t{f"R${num:.2f}".replace(".", ","):>10}")
    print(f"Dobro do valor: \t{dobro(num, True):>10}")
    print(f"Metade do preço: \t{metade(num, True):>10}")
    print(f"{p1}% de aumento: \t{aumentar(num, p1, True):>10}")
    print(f"{p2}% de redução: \t{diminuir(num, p2, True):>10}")
    
    print("-" * 30)
    
    