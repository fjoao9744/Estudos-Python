from tkinter import * #voltando pro habitual

tela = Tk()


l1 = Label(tela, text="linha 1")
l1.grid(row=0, column=0)

print(l1.configure().keys()) #verificar as caracteristicas da label

l1.config(fg="blue") #colocar a cor azul
l1.config(padx=50) # coloar um padding x de 50
l1.config(bg="purple") # colocar o fundo da label roxa

# l1.config(fg="blue", padx=50, bg="purple")


mainloop()
