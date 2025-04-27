from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = r"C:\Users\fjoao\Documents\GitHub\Estudos-Python\CursoEmVideo\desafios\desafio-115-1\lib\arquivo.txt"

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do sistema"])
    
    if resposta == 1:
        lerArquivo(arq)

    elif resposta == 2:
        cabeçalho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = leiaInt("Idade: ")
        
        cadastrar(arq, nome, idade)

    elif resposta == 3:
        cabeçalho("Saindo do sistema... até logo!")
        break
        
    else:
        print("\033[31mERRO! digite uma opção valida!\033[m")
        
    sleep(1)