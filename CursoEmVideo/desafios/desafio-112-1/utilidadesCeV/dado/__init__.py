def leiaDinheiro(text):
    valido = False
    while not valido:
        num = str(input(text)).replace(",", ".").strip()
        
        if num.isalpha() or num == "":
            print(f"\033[0;31mERRO: \"{num}\" é um preço invalido!\033[m]")
            
        else:
            valido = True
            return float(num)
        
def leiaInt(msg):
    ok = False
    valor = 0
    
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
            
        else:
            print("\033[0;31;mERRO! digite um numero inteiro valido!\033[m")
            
        if ok:
            break
    
    return valor