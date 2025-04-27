def linha(tamanho = 42):
    return "-" * tamanho
    
def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())
    
def menu(lista):
    cabeçalho("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print(f"\033[33m{c}\033[34m - {item}\033[m")
        c += 1
        
    print(linha())
    
    opc = leiaInt("\033[32mSua opção: \033[m")
    return opc
    
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