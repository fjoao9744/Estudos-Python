import os

nova_pasta = "teste2"
caminho = "C:\\Users\\fjoao\\Documents\\GitHub\\Estudos-Python"

caminho_completo = os.path.join(caminho, nova_pasta) # vai juntar esses dois caminho em 1
print(caminho_completo)

os.mkdir(caminho_completo) # cria a pasta