# 28. Eliminar duplicados manteniendo el orden
def unique_preserve(lst):
    nueva = []
    for item in lst:
        if item not in nueva:
            nueva.append(item)
    return nueva

