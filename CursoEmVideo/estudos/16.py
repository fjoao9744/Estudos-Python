
    #Modulo
import math
print(math.factorial(5))

    #Função recursiva
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)



