import flet as ft
from models import db, Data

# Conecta ao banco de dados e cria as tabelas
db.connect()
db.create_tables([Data], safe=True)

def main(page: ft.Page):
    page.title = "Registro de Frases"


    def enviar(event):
        # Cria um novo registro no banco de dados
        Data.create(nome=nome.value, palavra=palavra.value, preco=float(preco.value))
        atualizar()  # Atualiza a lista após adicionar um novo registro
        
        # Limpa os campos após o envio
        limpar()
        page.update()

    # Campos de entrada
    txt_nome = ft.Text("Qual o seu nome:")
    nome = ft.TextField(label="Digite o seu nome...", text_align=ft.TextAlign.LEFT)

    txt_palavra = ft.Text("Digite algo para enviar para o banco de dados:")
    palavra = ft.TextField(label="Digite algo...", text_align=ft.TextAlign.LEFT)

    txt_preco = ft.Text("Digite o preço:")
    preco = ft.TextField(value="0", label="Digite o preço do produto")

    # Botão para enviar os dados
    botao_send = ft.ElevatedButton("Enviar dados", on_click=enviar)
    def limpar():
        nome.value = ""
        palavra.value = ""
        preco.value = "0"

    # Adiciona os componentes à página
    page.add(
        txt_nome,
        nome,
        txt_palavra,
        palavra,
        txt_preco,
        preco,
        botao_send
    )

    # Lista para armazenar os itens de texto
    list_items = []

    # Função para atualizar a lista exibida
    def atualizar() -> None:
        # Limpa os itens anteriores
        for item in list_items:
            page.controls.remove(item)
        list_items.clear()  # Limpa a lista de itens de texto

        # Adiciona os novos dados
        for item in Data.select():
            text_item = ft.Text(f"{item.id} {item.nome} - {item.palavra} - {item.preco}")
            page.add(text_item)
            list_items.append(text_item)  # Armazena o item adicionado

        page.update()  # Atualiza a página para refletir as mudanças

    # Inicializa a lista com os dados existentes
    atualizar()

# Executa o aplicativo Flet
ft.app(target=main)
