from lib.interface import cabeçalho
from lib.arquivo import ler, criar, cadastrar


criar()
while True:
    menu = cabeçalho()
    
    if menu == 1:
        for line in ler():
            print(line)
        
    elif menu == 2:
        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))
        
        cadastrar(nome, idade)
        
    elif menu == 3:
        break