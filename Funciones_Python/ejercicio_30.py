# 30. Dividir una lista en sublistas de tamaño k
def chunk(lista, k):
    return [lista[i:i+k] for i in range(0, len(lista), k)]