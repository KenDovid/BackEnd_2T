# 9. Invertir una lista (sin usar reversed)
def invertir_lista(lst):
    invertida = []
    for i in range(len(lst) - 1, -1, -1):
        invertida.append(lst[i])
    return invertida

