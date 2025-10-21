# 24. Contar ocurrencias de cada elemento en una lista
def contar_ocurrencias(lista):
    conteo = {}
    for elemento in lista:
        if elemento in conteo:
            conteo[elemento] += 1
        else:
            conteo[elemento] = 1
    return conteo

