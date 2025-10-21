# 50. Aplicar función a listas en paralelo (como map + zip)
def zip_map(func, *lists):
    return [func(*args) for args in zip(*lists)]
