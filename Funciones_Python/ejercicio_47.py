# 47. Aplicar función a pares consecutivos
def pairwise_apply(func, lista):
    return [func(lista[i], lista[i+1]) for i in range(len(lista)-1)]

