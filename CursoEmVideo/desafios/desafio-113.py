def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
                
        except (ValueError, TypeError):
            print("\033[0;31mERRO: por favor, digite um numero valido\033[m")
            continue
        
        except (KeyboardInterrupt):
            print("\033[0;31m\nUsuario preferiu não digitar nada.\033[m")
            return 0
            
        else:
            return n
        
def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
            
        except (ValueError, TypeError):
            print("\033[0;31mERRO: por favor, digite um numero valido\033[m")
            continue
        
        except (KeyboardInterrupt):
            print("\033[0;31m\nUsuario preferiu não digitar nada.\033[m")
            return 0
        
        else:
            return n
            
num1 = leiaInt("Digite um numero inteiro: ")
num2 = leiaFloat("Digite um numero real: ")

print(f"O numero inteiro foi {num1} e o real foi {num2}")