import flet as ft
from models import db, Data

# Conecta ao banco de dados e cria as tabelas
db.connect()
db.create_tables([Data], safe=True)

def main(page: ft.Page):
    page.title = "Registro de Frases"

    data_list = ft.ListView()

    def enviar(event):
        # Cria um novo registro no banco de dados
        Data.create(nome=nome.value, palavra=palavra.value, preco=float(preco.value))
        data_list.controls.append(ft.Text(f"{nome.value} - {palavra.value} - {preco.value}"))

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


    for item in Data.select():
        text_item = ft.Text(f"{item.nome} - {item.palavra} - {item.preco}")
        data_list.controls.append(text_item)

    page.add(
        data_list
    )


# Executa o aplicativo Flet
ft.app(target=main)
