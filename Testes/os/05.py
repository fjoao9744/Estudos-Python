import os

print(os.path.basename(os.getcwd())) # mostrar o nome da pasta atual

print(os.path.dirname(os.getcwd())) # mostra o nome do diretorio

raiz = "teste os"
novas_pastas = "brasil\\ES\\Colatina"
caminho = os.path.join(raiz, novas_pastas)

os.makedirs(caminho) # cria varias pastas

