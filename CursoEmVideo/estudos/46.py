import os

texto = open('arquivo.txt', 'w')

texto.write('smogon')

texto = open('arquivo.txt', 'r', encoding='utf-8')

print(texto.read())


