# 64. Aplanar lista anidada recursivamente
def flatten_rec(lista_anidada):
    resultado = []
    for elemento in lista_anidada:
        if isinstance(elemento, list):
            resultado.extend(flatten_rec(elemento))
        else:
            resultado.append(elemento)
    return resultado

