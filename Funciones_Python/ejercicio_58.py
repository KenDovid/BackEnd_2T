# 58. Crear varias funciones que recuerdan su índice
def closure_factory(n):
    funciones = []
    for i in range(n):
        funciones.append(lambda i=i: print(f"Soy la función {i}"))
    return funciones

