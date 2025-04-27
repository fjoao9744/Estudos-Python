def linha(tamanho):
    print("-" * tamanho)
    
def cabeçalho():
    linha(42)
    print(f"{"MENU PRINCIPAL":^42}")
    linha(42)
    
    print("1 - Ver pessoas cadastradas")
    print("2 - Cadastrar nova pessoa")
    print("3 - Sair do sistema")
    
    linha(42)
    
    op = leiaInt("Sua opção: ")
    
    return op
    
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