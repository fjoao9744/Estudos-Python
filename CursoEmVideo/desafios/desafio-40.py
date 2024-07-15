n1 = float(input('qual foi a primeira nota? '))
n2 = float(input('qual foi a segunda nota? '))
media = (n1 + n2)//2

if media < 5.0:
    print('a media das notas foi {},\033[0;31;40m reprovou! \033[m'.format(media))
elif media >= 5.0 <= 6.9:
    print('a media das notas foi {}, esta de recuperação!'.format(media))
else:
    print('a media das notas foi {}, passou,\033[0;35;40m parabens!\033[m'.format(media))