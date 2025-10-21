# 27. Devolver primer y último elemento de una lista
def primer_y_ultimo(lista):
    if not lista:
        return None
    return lista[0], lista[-1]

