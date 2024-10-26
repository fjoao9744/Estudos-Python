import tkinter as tk
from PIL import Image, ImageTk

app = tk.Tk()
app.geometry("1000x600")
app.title("Smogon")

imagem = Image.open("D:\Meus Documentos\Aluno\Desktop\Otávio\smogon.png") #imagem

imagem_tk = ImageTk.PhotoImage(imagem)

def press_button() -> None:
    label = tk.Label(app, image=imagem_tk).grid(row=2, column=0)


button = tk.Button(app, text="aperte aqui", command=press_button)

button.grid(row=1, column=0, padx=475)

app.mainloop()
