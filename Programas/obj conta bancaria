class ContaBancaria:
    def __init__(self, titular, saldo, numero):
        self.titular = titular
        self.saldo = saldo
        self.numero = numero
        
    def depositar(self, valor):
        self.saldo += valor
        print(f"Você depositou {valor}, agora você tem {self.saldo}")
        
    def sacar(self, valor):
        self.saldo -= valor
        print(f"Você sacou {valor} reais, agora voce tem {self.saldo}")
        
    def ver_saldo(self):
        print(f"Seu saldo é de {self.saldo}")
        
def gerar_numero():
    contador = 0
    while True:
        contador += 1
        yield contador
        
joao = ContaBancaria("joao", 100, gerar_numero())

joao.ver_saldo()

joao.depositar(500)
joao.sacar(50)

joao.ver_saldo()