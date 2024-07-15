n1 = str(input('digite uma frase: ')).strip().upper()
divide = n1.split()
junta = ''.join(divide)
inverso = junta[::-1]

'''for c in range(len(junta) -1, -1, -1):
    inverso += junta[c]'''

if inverso == junta:
    print('você digitou {}, aocontrario fica {}, que é um palidromo '.format(junta, inverso))
else:
    print('você digitou {}, aocontrario fica {}, que NÃO é um palidromo '.format(junta, inverso))

