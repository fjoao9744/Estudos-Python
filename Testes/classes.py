class Player():
    def __init__(self, nome, level, andar, hp):
        self.nome = nome
        self.level = 1
        self.andar = 0
        self.hp = 20

    def dano(self, dano):
        self.hp -= dano
    
    def gameover(self, morte):
        if self.hp <= 0:
            print('game over')
        else:
            print(f'o player {self.nome} esta vivo')


player1 = Player('smogon')

print(player1.nome)