def leiaint():
    while True:
    
        num = input("Digite um numero: ")
        
        if not num.isnumeric():
            print("Digite um numero valido")
            continue
            
        return int(num)
    
n = leiaint()

print(f"Você acabou de digitar o numero: {n}")

