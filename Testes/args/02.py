def printar_itens(**kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)

printar_itens(smogon = "2x", idade = 19, barba = True)

