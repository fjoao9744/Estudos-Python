import json
from deposit import *

with open('alunos.json', 'wt') as alunos:
    alunos = alunos

while True:
    @separar
    def lista_de_alunos():
        return alunos
    op = int(input('oque deseja: \n[0]criar novo alunos \n[1]abrir aluno existente'))

    if op == 0:
        nome = str(input('digite o nome do aluno: '))
        with open('alunos.json', 'w') as alunos:
            alunos.write(nome)

            
