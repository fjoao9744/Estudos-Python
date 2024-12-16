""" Codigo normal """

class Pessoa1:
    def __init__(self, nome):
        self.nome = nome


print("==pessoa1==")

joao1 = Pessoa1("joao")

print(joao1.nome)

joao1.nome = ""

print(joao1.nome)

""" Codigo com getter e setter """

class Pessoa2:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self): # isso agora é um getter
        return self.__nome

    @nome.setter
    def nome(self, new_name): # isso é um setter
        if new_name.strip() == "":
            print("você não pode colocar um nome vazio")
            return

        self.__nome = new_name

    @nome.deleter
    def nome(self): # isso é um deleter
        print("deletando o nome...")
        self.__nome = None

print("==pessoa2==")

joao2 = Pessoa2("joao")

print(joao2.nome)

joao2.nome = ""
joao2.nome = "smogon"

print(joao2.nome)

del joao2.nome

print(joao2.nome)