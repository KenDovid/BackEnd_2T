# 38. Dividir texto en líneas de máximo n caracteres (sin cortar palabras)
def wrap_text(text, n):
    palabras = text.split()
    lineas = []
    linea_actual = ""
    for palabra in palabras:
        if len(linea_actual) + len(palabra) + 1 <= n:
            linea_actual += (" " if linea_actual else "") + palabra
        else:
            lineas.append(linea_actual)
            linea_actual = palabra
    if linea_actual:
        lineas.append(linea_actual)
    return lineas

