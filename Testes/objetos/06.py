class Humano:
    def __init__(self, nome, vida):
        self.vida = vida
        self.nome = nome
    
    def falar(self):
        print(f"{self.nome} esta falando")

class Player(Humano):
    def __init__(self, nome, vida, atk):
        super().__init__(nome, vida)

    def falar(self):
        print(f"O player esta falando") # esse metodo esta substituindo o da classe mãe

jog = Player("Joao", 20, 2)

jog.falar()