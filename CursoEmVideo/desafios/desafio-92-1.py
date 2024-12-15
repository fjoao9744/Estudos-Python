from datetime import datetime

dados = dict()
dados["nome"] = str(input("Digite seu nome: "))
nasc = int(input("Digite seu ano de nascimento: "))
dados["idade"] = datetime.now().year - nasc
dados["ctps"] = int(input("Carteira de trabalho(0 se não tem) "))

if dados["ctps"] != 0:
    dados["contratação"] = int(input("Qual foi seu ano de contratação: "))
    dados["salario"] = float(input("Qual é o seu salario: "))

    dados["aposentadoria"] = dados["idade"] + ((dados["contratação"] + 35) - datetime.now().year)

print("=-" * 20)

for k, v in dados.items():
    print(f"{k} tem o valor {v}")