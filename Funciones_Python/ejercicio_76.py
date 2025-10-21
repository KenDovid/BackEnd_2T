# 76. Verificar tipo de dato
def check_type(x, t):
    if not isinstance(x, t):
        raise TypeError(f"Se esperaba {t}, se recibió {type(x)}")
    return True

