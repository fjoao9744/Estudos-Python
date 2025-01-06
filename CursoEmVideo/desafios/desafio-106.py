def escrever(string):

    print("~" * (len(string) + 4))
    print(f"  {string}")
    print("~" * (len(string) + 4))


while True:
    escrever("Sistema de ajuda PyHelp")
    obj = str(input("Digite uma função ou uma biblioteca: ")).strip()
    eval(f"help({obj})")
    