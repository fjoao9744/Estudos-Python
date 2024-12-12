pessoa = {}

pessoa["nome"] = str(input("Digite seu nome: ")).strip().capitalize()
pessoa["idade"] = 2024 - int(input("Digite o ano do seu nascimento: "))
pessoa["clt"] = int(input("Digite sua carteira de trabalho: (0 se não tiver) "))

if pessoa['clt'] != 0:
    pessoa["ano_contratação"] = int(input("Qual foi seu ano de contratação: "))
    pessoa["salario_contratação"] = int(input("Qual é o seu salario: "))

print("-=" * 10)
print(pessoa)
print(f"Você tem {pessoa['idade']} anos")
if pessoa['clt'] != 0:
    print(f"Sua carteira de trabalho é {pessoa['clt']}")
    print(f"Você foi contratado em {pessoa['ano_contratação']}")
    print(f"E vai se aposentar com {pessoa['idade'] + (35 - (2024 - pessoa['ano_contratação']))} anos")
    print(f"Ganha {pessoa['salario_contratação']}")



