# 29. Separar lista según predicado (True/False)
def partition(lista, pred):
    verdaderos = []
    falsos = []
    for item in lista:
        if pred(item):
            verdaderos.append(item)
        else:
            falsos.append(item)
    return verdaderos, falsos

