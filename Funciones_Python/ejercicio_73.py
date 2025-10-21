# 73. Leer líneas de un archivo con manejo de error
def read_file_lines(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        print("Archivo no encontrado.")
        return []

