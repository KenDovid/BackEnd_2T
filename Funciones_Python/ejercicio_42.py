# 42. Emular filter(): devolver lista con elementos que cumplen el predicado
def filter_custom(pred, lista):
    return [x for x in lista if pred(x)]

