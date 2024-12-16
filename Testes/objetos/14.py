class Coleção:
    def __init__(self):
        self.itens = list()

    def add_item(self, item):
        self.itens.append(item)

    def __contains__(self, item):
        return item in self.itens

    def __str__(self):
        return str(self.itens)

col = Coleção()

col.add_item(3)
col.add_item(2)
col.add_item(0)

print(col)

print(1 in col)
print(2 in col)

