from tkinter import *

def enviar_mensagem():
    mensagem = entrada.get()
    if mensagem:
        listbox.insert(END, f"You: {mensagem}")  # Adiciona a mensagem
        entrada.delete(0, END)  # Limpa a entrada

root = Tk()
root.geometry("400x300")

# Cria um Listbox para exibir as mensagens
listbox = Listbox(root)
listbox.place(x=10, y=10, width=380, height=200)  # Define a posição e tamanho

# Cria uma entrada para novas mensagens
entrada = Entry(root)
entrada.place(x=10, y=220, width=280)  # Posição da entrada

# Cria um botão para enviar mensagens
botao_enviar = Button(root, text="Enviar", command=enviar_mensagem)
botao_enviar.place(x=300, y=220)  # Posição do botão

root.mainloop()
