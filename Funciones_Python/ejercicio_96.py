# 96. Frecuencia de palabras en texto
def word_frequency(path, top_n=10):
    from collections import Counter
    with open(path, "r", encoding="utf-8") as f:
        palabras = f.read().lower().split()
    conteo = Counter(palabras)
    return conteo.most_common(top_n)

