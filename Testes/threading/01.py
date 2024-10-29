from tkinter import *
import threading
from time import sleep

tela = Tk()

list1 = Listbox(tela)
list1.pack()
list2 = Listbox(tela)
list2.pack()

def l1():
    while True:
        list1.insert(END, "smogon")
        sleep(1)

def l2():
    while True:
        list2.insert(END, "smogon")
        sleep(2)

thread1 = threading.Thread(target=l1) #define oque o thread vai rodar
thread2 = threading.Thread(target=l2)

thread1.start() #faz o thread rodar
thread2.start()

mainloop()
