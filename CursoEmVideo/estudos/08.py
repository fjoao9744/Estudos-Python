nome = str(input('\033[0;36;40mdigite o seu nome:\033[m '))
if nome == 'maria':
    print('irmã')
elif nome == 'hendrick' or 'moises':
    print('amigo')

else:
    print('ninguem especial')
print('Bom dia {}!'.format(nome))