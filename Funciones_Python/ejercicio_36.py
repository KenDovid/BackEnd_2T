# 36. Extraer números enteros de un texto
def extract_numbers(s):
    numeros = []
    actual = ""
    for c in s:
        if c.isdigit():
            actual += c
        elif actual:
            numeros.append(int(actual))
            actual = ""
    if actual:
        numeros.append(int(actual))
    return numeros

