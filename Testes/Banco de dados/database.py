from peewee import * #importando tudo do peewee(ORM)

db = SqliteDatabase('smogon.db') #criando o banco de dados SQLite

class Usuario(Model): #tabela de usuarios(quando você coloca model entre parenteses você esta dizendo que isso vai ser uma tabela)
    nome = CharField() #charfield é um campo de texto
    email = CharField(unique=True) #o unique=True serve para impedir a inserção de um email ja existente
    senha = CharField()
    #lembrando que o peewee ja gera o id automaticamente

    class Meta:
        database = db #serve para o pewee entender em qual banco de dados essa tabela vai conversar

class Anuncio(Model):
    usuario = ForeignKeyField(Usuario, backref='usuarios') #a chave estrangeira | o backref serve para criar um prefixo 
    titulo = CharField()
    descricao = TextField() #o textfield não tem limite de caracteres
    valor = DecimalField() #representa o valor a ser pago ou seja, um umero decimal

    class Meta:
        database = db

