n1 = float(input('digite uma distância em metros '))
print('a medida de {} metros corresponde a:'.format(n1))
print('{}km \n{}hm \n{}dam \n{}dm \n{}cm \n{}mm'.format((n1/1000), (n1/100), (n1/10), (n1*10), (n1*100), (n1*1000)))
