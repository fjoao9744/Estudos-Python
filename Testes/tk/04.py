from tkinter import *
from turtle import *

tela = Tk()

def circulo():
    donatello = Turtle()
    donatello.color("purple")
    donatello.shape("turtle")
    donatello.circle(50)

    mainloop()

def quadrado():
    donatello = Turtle()
    donatello.shape("turtle")
    donatello.color("purple")
    for c in range(4):
        donatello.forward(100)
        donatello.right(-90)

    mainloop()

def triangulo():
    donatello = Turtle()
    donatello.shape("turtle")
    donatello.color("purple")
    for c in range(3):
        donatello.forward(100)
        donatello.right(-120)


    mainloop()


Button(tela, text="circle", command=circulo).grid(row=0, column=0)
Button(tela, text="square", command=quadrado).grid(row=0, column=1)
Button(tela, text="triangle", command=triangulo).grid(row=0, column=2)



tela.mainloop()
