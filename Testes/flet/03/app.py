import flet as ft
from models import db, Data
from peewee import *

db.connect()
db.create_tables([Data])

def main(page: ft.Page):

    page.title = "registro de frases"

    def enviar(event):

        Data.create(nome=nome.value, palavra=palavra.value, preco=preco.value)
        
        

        print("smogon")




    txt_nome = ft.Text("Qual o seu nome:")
    nome = ft.TextField(label="digite o seu nome...", text_align=ft.TextAlign.LEFT)

    txt_palavra = ft.Text("Digite algo para enviar para o banco de dados:")
    palavra = ft.TextField(label="digite algo...", text_align=ft.TextAlign.LEFT)

    txt_preco = ft.Text("Digite o preço:")
    preco = ft.TextField(value="0", label="digite o preço do produto")

    botao = ft.ElevatedButton("Enviar dados", on_click=enviar)



    page.add(
        txt_nome,
        nome, 

        txt_palavra,
        palavra,

        txt_preco,
        preco,

        botao

    )

ft.app(target=main)