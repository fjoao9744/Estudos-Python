import time

def separar(func):
    def wrapper():
        print('-' * 20)
        func()
        print('-' * 20)
        
    return wrapper
    
def tempo(func):
    def wrapper():
        inicio = time.time()
        func()
        final = time.time()
        print(final - inicio)
        
    return wrapper
    

@tempo
def soma():
    print(1 + 1)
    
@separar
def escrever():
    print('smogon')


soma()

    
