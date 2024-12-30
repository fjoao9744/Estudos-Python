def area(altura, largura):
    print(f"A area de um terreno {altura}x{largura} é de {altura * largura}m²")
print("Controle ")
print("-" * 20)

l = float(input("LARGURA (m): "))
a = float(input("COMPRIMENTO (m): "))

area(l, a)
