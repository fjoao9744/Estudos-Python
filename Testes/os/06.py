import os

print(os.path.exists("Testes")) # verifica se algum caminho existe
print(os.path.exists("Testes\\os\\06.py"))
print(os.path.exists("Testes\\os\\00.py"))

"""
tambem podemos usar o path.isdir() para verificar se é uma pasta e path.isfile() pra verificar se é um arquivo

"""