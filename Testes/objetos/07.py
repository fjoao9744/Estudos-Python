from abc import ABC, abstractmethod

class Animal(ABC): # "esqueleto" das outras classes

    @abstractmethod
    def falar(self):
        pass

    @abstractmethod
    def comer(self):
        pass

class Humano(Animal):
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print(f"Ola meu nome é {self.nome}")

    def comer(self):
        pass

class Cachorro(Animal):
    def falar(self):
        print("Au au!")

    def comer(self):
        pass

joao = Humano("joao")

joao.falar()
joao.comer()


