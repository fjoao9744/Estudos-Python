filho = 3
medfil = medfil2 = 0

for f in range(1, filho + 1):
                medfil = int(input('qual a idade do seu {}º filho?'.format(f)))
                medfil2 += medfil
print('a media de idade dos seus filhos é de {}'.format(medfil2 // filho))