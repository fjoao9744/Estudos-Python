def decorador(func):
    def wrapper():
        print("estou no decorador!")
        func()
        
    return wrapper

@decorador
def função():
    print("Estou na função")

função()