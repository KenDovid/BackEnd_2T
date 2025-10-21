# 69. Permutaciones recursivas de una cadena
def permutations_rec(s):
    if len(s) <= 1:
        return [s]
    resultado = []
    for i, letra in enumerate(s):
        for perm in permutations_rec(s[:i] + s[i+1:]):
            resultado.append(letra + perm)
    return resultado

