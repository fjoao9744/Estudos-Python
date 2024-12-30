import random
import time
numeros = []

def sortear(list_num):
    print(f"Sorteando 5 valores aleatorios: ", end='')
    for c in range(5):
        random_num = random.randint(0, 10)
        list_num.append(random_num)
        print(random_num, end=" ")
        time.sleep(0.5)
    print("PRONTO!")
        
def soma_par(list_num):
    list_even = []
    for c in list_num:
        if c % 2 == 0:
            list_even.append(c)
    print(f"A soma de todos os numeros pares foi de {sum(list_even)}")
    

sortear(numeros)
soma_par(numeros)