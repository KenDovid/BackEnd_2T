# 95. Estadísticas de texto desde archivo
def text_stats(path):
    with open(path, "r", encoding="utf-8") as f:
        texto = f.read()
    palabras = texto.split()
    oraciones = texto.count(".")
    parrafos = texto.count("\n\n") + 1
    promedio = sum(len(p) for p in palabras) / len(palabras)
    return {
        "palabras": len(palabras),
        "oraciones": oraciones,
        "parrafos": parrafos,
        "promedio_longitud": round(promedio, 2)
    }

