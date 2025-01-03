from time import sleep

def maior(*num):
    cont = maior = 0 
    print("\nAnalisando os valores passados")
    for v in num:
        print(v, end=" ", flush=True)
        sleep(0.3)
        if cont == 0:
            maior = v
            
        else:
            if v >= maior:
                maior = v
        cont += 1
    print(f"foram informador {cont} valores")
    print(f"o maior valor informado foi {maior}")
    
        
maior(1, 2, 3, 9, 4, 7, 5)

