# 60. Closure que alterna entre True y False
def toggle(initial=False):
    estado = initial
    def cambiar():
        nonlocal estado
        estado = not estado
        return estado
    return cambiar
