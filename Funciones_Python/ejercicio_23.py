# 23. Filtrar cadenas con longitud mayor o igual a n
def filtrar_longitud(lista, n):
    return [palabra for palabra in lista if len(palabra) >= n]


