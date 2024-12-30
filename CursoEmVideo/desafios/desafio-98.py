from time import sleep

def contador(inicio, fim, passo = 1):
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    
    if inicio > fim and passo > 0:
        passo -= passo * 2
        
    if passo == 0:
        passo = 1
        
    for c in range(inicio, fim + passo, passo):
        print(c, end=" ")
        sleep(0.3)
    print("FIM!")

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
