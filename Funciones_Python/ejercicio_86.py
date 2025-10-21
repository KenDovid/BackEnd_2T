# 86. Decorador que asegura argumentos no negativos
def ensure_non_negative(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError("Argumento negativo no permitido")
        return func(*args, **kwargs)
    return wrapper

