def escreva(txt):
    for c in range(len(txt) + 2):
        print("~", end='')
    print()
    print(f" {txt}")
    for c in range(len(txt) + 2):
        print("~", end='')
    print()

escreva("Gustavo Guanabara")
escreva("Curso de Python no Youtube")
escreva("CeV")