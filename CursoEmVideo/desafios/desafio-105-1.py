def notas(*args, sit=False):
    """
    notas(*args, sit=False)
    :param *args: uma ou mais notas. (aceita varias)
    :param sit: (opcional) indicase deve ou não mostrar a situação.
    :return: retorna as informações sobre a turma.
    """
    r = dict()
    r["total"] = len(args)
    r["maior"] = max(args)
    r["menor"] = min(args)
    r["media"] = sum(args) / len(args)
    
    if sit:
        if r["media"] >= 7:
            r["sit"] = "boa"
            
        elif r["media"] >= 5:
            r["sit"] = "razoavel"

        else:
            r["sit"] = "ruim"
            
    return r

print(notas(1.9, 9, 1.0, 3.4))