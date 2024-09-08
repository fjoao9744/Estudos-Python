from database import db, Usuario, Anuncio

db.connect() #conecta no banco de dados

db.create_tables([Usuario, Anuncio]) #criar as tabelas caso não estejam criadas

'''
maria = Usuario.get(Usuario.email == 'mariasmogon@gmail.com') #pega o usuario pelo email

maria.nome = "Maria smogon" #altera o nome do usuario
maria.save() #salva as alterações no banco de dados
'''
'''
try:
    Usuario.create(nome='teste', email='hendricksmogon@gmail.com', senha='12345')
except:
    print('email ja existente tente colocar outro')
'''

'''
deletar_usuario = Usuario.get(Usuario.email == 'hendricksmogon@gmail.com')
deletar_usuario.delete_instance()
'''
lista_usuarios = Usuario.select() #selecionando os itens da tabela

for _ in lista_usuarios: #percorre a tabela selecionada
    print('-', _.id, _.nome, _.email) #mostra ela na tela