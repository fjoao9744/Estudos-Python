from time import sleep

def contador(inicio, fim, passo=1):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
        
    cont = inicio
    
    if inicio < fim:
        cont = inicio
        
        while cont <= fim:
            print(cont, end=" ", flush=True)
            sleep(0.5)
            cont += passo
        print("FIM")
    
    else:
        cont = inicio
        
        while cont >= fim:
            print(cont, end=" ", flush=True)
            sleep(0.5)
            cont -= passo
        print("FIM")
    
print("-=" * 20)
contador(1, 10)
print("-=" * 20)
contador(10, 0, 2)
print("-=" * 20)
print("Agora é sua vez de personalizar: ")
inicio = int(input(f"{"Inicio:":<10}"))
fim = int(input(f"{"Fim:":<10}"))
passo = int(input(f"{"Passo:":<10}"))

contador(inicio, fim, passo)