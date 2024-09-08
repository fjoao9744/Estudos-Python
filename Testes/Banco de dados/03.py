from database import db, Usuario, Anuncio

db.connect() #conecta no banco de dados

db.create_tables([Usuario, Anuncio]) #criar as tabelas caso não estejam criadas

davi = Usuario.get(Usuario.email == 'davismogon@gmail.com')


'''
anuncio = Anuncio.create( #essa variavel anuncio vai receber a tabela anuncio
    usuario = davi, #o usuario é uma chave estrangeira por isso passamos o objeto do davi inteiro
    titulo = 'video do banco de dados', 
    descricao = 'o projeto é crair um banco de dados com o peewee',
    valor = 30.0
)'''
'''
#anuncios de davi
anuncios_davi = Anuncio.select().join(Usuario).where(Usuario.email == 'davismogon@gmail.com')
#essa variavel vai selecionar a tabela de anuncios junto com a tabela de usuarios e vai filtrar pelo email

for _ in anuncios_davi:
    print('-', _.id, _.titulo, _.valor)

'''
print(Anuncio.select().count()) #codigo pra mostrar quantos anuncios tem
Anuncio.delete().execute() #codigo para deletar TUDO
print(Anuncio.select().count())

