def criar():
    try:
        open(r"C:\Users\fjoao\Documents\GitHub\Estudos-Python\CursoEmVideo\desafios\desafio-115\lib\arquivo.txt", "x")
        
    except:
        ...
        
    else:
        print("Arquivo criado com sucesso")
        
def ler():
    with open(r"C:\Users\fjoao\Documents\GitHub\Estudos-Python\CursoEmVideo\desafios\desafio-115\lib\arquivo.txt", "r") as arq:
        return arq.readlines()
    
def cadastrar(nome, idade):
    with open(r"C:\Users\fjoao\Documents\GitHub\Estudos-Python\CursoEmVideo\desafios\desafio-115\lib\arquivo.txt", "at+") as arq:
        arq.write(f"{nome} : {idade}")