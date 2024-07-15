'''from math import sqrt
co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
print('a hipotenusa vai medir {:.2f}'.format(sqrt((co*co)+(ca*ca))))'''
from math import hypot
co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente '))
print('a hipotenusa vai medir {:.2f}'.format(hypot(co, ca)))

