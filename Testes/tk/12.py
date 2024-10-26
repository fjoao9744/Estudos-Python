# importação de bibliotecas
from tkinter import *
from tkinter.font import Font

# criação e configuração da tela
screen = Tk()
screen.config(bg="grey")
screen.state("zoomed")
screen.title("FaceSmogon")

# fontes personalizadas
FONT = Font(family="Candara", size=15)
TITLE_FONT = Font(family="Candara", size= 30, weight="bold")
BUTTON_FONT =Font(family="Candara", size= 11)

# titulo
Titulo = Label(screen, text="FaceSmogon", bg="grey", font=TITLE_FONT)
Titulo.pack(anchor=W, side=TOP)

# aba de envio de mensagem
message_frame = Frame(screen, bg="grey")
message_frame.pack(side=BOTTOM, pady=(0, 100))

message_entry = Entry(message_frame, width=70, font=FONT, relief=GROOVE, bd=4)
message_entry.pack(side=LEFT)

message_send_button = Button(message_frame, text="send", font=BUTTON_FONT, relief=GROOVE, bd=4, highlightthickness=0)
message_send_button.pack(side=LEFT, padx=(10, 0))


mainloop()