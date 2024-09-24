import flet as ft

def main(page: ft.Page):

    page.title = "registro de frases"

    def enviar(event):
        pass

    txt_nome = ft.Text("Qual o seu nome:")
    nome = ft.TextField(label="digite o seu nome...", text_align=ft.TextAlign.LEFT)

    txt_palavra = ft.Text("Digite algo para enviar para o banco de dados:")
    palavra = ft.TextField(label="digite algo...", text_align=ft.TextAlign.LEFT)

    botao = ft.ElevatedButton("Enviar dados", on_click=enviar)

    page.add(
        txt_nome,
        nome, 

        txt_palavra,
        palavra,

        botao
    )

ft.app(target=main)