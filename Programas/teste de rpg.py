itens = {

    "minerios" : {"pedra": "pedra", "ouro": "ouro", "lapis": "lapis"}, 
    "itens" : {"madeira": "madeira","corda": "corda"}

        }

class Inventario:
    def __init__(self, *itens):
        self.itens = list(itens)

    def add_item(self, item, rank, descrição= "Nenhuma"):
        rank = rank.upper()
        if rank not in "ABC":
            print("O rank do item é invalido, os unicos ranks suportados são A B e C")
            return

        self.itens.append((item, rank, descrição))

    def exibir(self):

        if len(self.itens) > 0:
            print("Lista de itens:")
            for i, _ in enumerate(self.itens):
                print(f"{i}- {_[0]}| rank {_[1]}")
            indice = int(input("Você quer ler a descrição de algum item? se sim, digite o numero dele: "))
            if 0 <= indice < len(self.itens):
                print(self.itens[indice][2])

        else:
            print("Não possui nenhum item no inventario")

class Humano:
    def __init__(self, nome):
        self.nome = nome.capitalize()

    def falar(self, fala):
        print(f"{self.nome} falou: {fala}")

class Npc(Humano):
    def __init__(self, nome):
        super().__init__(nome)


class Ferreiro(Npc):
    def __init__(self, nome):
        super().__init__(nome)

    def juntar_itens(self, player, *items):
        if len(items) == 3:
            print(items)
            if "madeira" in items and "pedra" in items and "corda" in items:
                print(f"{self.nome} criou um escudo de madeira para você")
                player.add_inv("Escudo de madeira", "C", "Um escudo feito para combate")
                
class Player(Npc):
    def __init__(self, nome):
        super().__init__(nome)
        self.inventario = Inventario()

    def interagir(self, npc):
        print(f"{self.nome} interagiu com {npc.nome}")

    def add_inv(self, *item):
        self.inventario.add_item(item)

inv = Inventario()

inv.add_item("Peitoral de prata", "C", "Este peitoral é feito de uma pedra rarissima(pedra de prata) encontrada nas minas do pais begarite(cidade - labirinto de rapã)")
inv.add_item("Espada de lagarto", "B", "Uma espada feita totalmente de escamas de lagartos")
inv.add_item("Escudo de madeira", "C", "Um escudo feito para combate")
inv.add_item("Cajado de invocação", "A", "Este cajado foi feito por um ferreiro da cidade central Millichiom")

francisco = Player("rudeus grerayt")
npc = Ferreiro("Jazz")

francisco.interagir(npc)

npc.juntar_itens(francisco, itens["minerios"]["pedra"], itens["itens"]["madeira"], itens["itens"]["corda"])