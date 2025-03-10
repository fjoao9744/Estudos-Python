from time import sleep

c = ['\033[m', # sem cor
     '\033[0;30;41m', # vermelho
     '\033[0;30;42m', # verde
     '\033[0;30;43m', # amarelo
     '\033[0;30;44m', # azul
     '\033[0;30;45m', # roxo
     '\033[7;30m' # branco
     ]

def ajuda(com):
    titulo(f"acessando o manual do comando: \'{com}\'", 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)
    

def titulo(msg, cor = 0):
    tamanho = len(msg) + 4
    
    print(c[cor], end="")
    print("~" * tamanho)
    print(f"  {msg}  ")
    print("~" * tamanho)
    print(c[0], end="")
    sleep(1)

comando = ''
while True:
    titulo("SISTEMA DE AJUDA PYHELP", 2)
    comando = str(input("Função ou biblioteca -> "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
        
titulo("ATÉ LOGO!", 1)