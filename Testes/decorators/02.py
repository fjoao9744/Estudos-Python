def decorador(func):
    def wrapper(*args, **kwargs): # usamos esse padrão quando a função tem parametros
        print("estou no decorador!")
        func(*args, **kwargs)
        
    return wrapper

@decorador
def função(palavra): # tem parametros
    print("Estou na função")
    print("palavra: ", palavra)

função("smogon")