# 91. Leer CSV y devolver lista de diccionarios
def parse_csv(path, sep=','):
    datos = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            encabezados = f.readline().strip().split(sep)
            for linea in f:
                valores = linea.strip().split(sep)
                datos.append(dict(zip(encabezados, valores)))
    except FileNotFoundError:
        print("Archivo no encontrado.")
    return datos

