lampada = {'funcionando':False,'plugada':False,'queimada':False}
#lampada funcionando?
if lampada['funcionando'] == False:
    #lampada plugada?
    if lampada['plugada'] == False:
        lampada['plugada'] = True
    #lampada queimada?
    elif lampada['queimada'] == False:
        lampada['queimada'] = True
    else:
        #trocando lampada
        lampada['funcionando'] = True

else:
    print('👍')

