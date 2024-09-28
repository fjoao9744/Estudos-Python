from peewee import *

db = SqliteDatabase('data.db')

class Data(Model):
    nome = TextField()
    palavra = TextField()
    preco = DecimalField()

    class Meta:
        database = db




