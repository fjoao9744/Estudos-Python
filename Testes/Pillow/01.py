#errado

from PIL import Image as img

iniciais = ["bulbasaur", "squirtle", "charmader"]

for i, c in enumerate(iniciais):
    print(i, c)

n = int(input("qual inicial você quer ver? "))

if n == 0:
    with img("imagens/bulbasaur.png") as im:
        im.show()