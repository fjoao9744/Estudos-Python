def notas(*args, sit = False):
    """
    notas(*args, sit=False)
    :param *args: uma ou mais notas. (aceita varias)
    :param sit: (opcional) indicase deve ou não mostrar a situação.
    :return: retorna as informações sobre a turma.
    """
    analise = {
        "total": len(args),
        "maior": max(args),
        "menor": min(args),
        "media": sum(args) / len(args)
    }
    if sit:
        if analise["media"] >= 8:
            analise["sit"] = "excelente"
            
        elif 7 < analise["media"] < 8:
            analise["sit"] = "boa"
            
        elif 4 < analise["media"] <= 7:
            analise["sit"] = "ruim"

        elif 0 < analise["media"] <= 4:
            analise["sit"] = "pessimo"
            
    return analise
    
    
print(notas(2, 4, sit=True))

