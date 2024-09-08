from database import db, Usuario, Anuncio

db.connect() #conecta no banco de dados

db.create_tables([Usuario, Anuncio]) #criar as tabelas caso não estejam criadas

#usuario = Usuario.create(nome="Smogon", email="hendricksmogon@gmail.com", senha="smogon123") #serve para criar um novo usuario na tabela
#Usuario.create(nome="Maria", email="mariasmogon@gmail.com", senha="smogon123")
#Usuario.create(nome="jose", email="josesmogon@gmail.com", senha="smogon123")
#Usuario.create(nome="davi", email="davismogon@gmail.com", senha="smogon123")

''' Select
lista_usuarios = Usuario.select() #selecionando os itens da tabela

for _ in lista_usuarios: #percorre a tabela selecionada
    print('-', _.id, _.nome, _.email) #mostra ela na tela
'''
''' Get
usuario1 = Usuario.get(Usuario.id == 2) #vai procurar e pegar o usuario de id 2

print(usuario1.id, usuario1.nome) #motra o id e o nome dele
'''

jose = Usuario.get(Usuario.email == 'josesmogon@gmail.com') #vai procurar e pegar o usuario com o email igual

print(jose.id, jose.nome) #motra o id e o nome dele


