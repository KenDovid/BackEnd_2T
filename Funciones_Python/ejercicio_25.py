# 25. Aplanar una lista de listas (1 nivel)
def flatten(lista_de_listas):
    resultado = []
    for sublista in lista_de_listas:
        for item in sublista:
            resultado.append(item)
    return resultado

