from turtle import * 
import os
donatello = Turtle() 
donatello.shape('turtle')

while True:
    n = input('digite pra onde deseja andar:')
    os.system('cls')
    
    if n == 'd':
        donatello.right(90)

    if n == 's':
        donatello.right(180)
    if n == 'a':
        donatello.right(-90)

    if n == 'w':
        donatello.right(0)
    

    
      
done() 