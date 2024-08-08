nota1 = float(input('nota 1: '))
nota2 = float(input('nota 2: '))
nota3 = float(input('nota 3: '))
faltas = int(input('Faltas: '))
media = (nota1 + nota2 + nota3) / 3

if (media >= 60 and faltas < 25):
    print("Aprovado!")



else:
    print("Reprovado!")
