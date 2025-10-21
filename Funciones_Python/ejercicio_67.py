# 67. Búsqueda binaria recursiva
def binary_search_rec(lista, objetivo, inicio=0, fin=None):
    if fin is None:
        fin = len(lista) - 1
    if inicio > fin:
        return -1
    medio = (inicio + fin) // 2
    if lista[medio] == objetivo:
        return medio
    elif lista[medio] > objetivo:
        return binary_search_rec(lista, objetivo, inicio, medio - 1)
    else:
        return binary_search_rec(lista, objetivo, medio + 1, fin)

