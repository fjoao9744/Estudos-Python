import moeda

p = float(input("Digite o preço: "))
print(f"A metade de {p} é {moeda.metade(p, True)}")
print(f"O dobro de {p} é {moeda.dobro(p, True)}")
print(f"Aumentando 10%, temos {moeda.aumentar(p, 10, True)}")
print(f"Diminuindo 13%, temos {moeda.diminuir(p, 13, True)}")