# 87. Decorador que cachea resultado en archivo
def cache_to_file(func):
    import os, pickle
    def wrapper(*args, **kwargs):
        nombre = f"{func.__name__}_cache.pkl"
        if os.path.exists(nombre):
            with open(nombre, "rb") as f:
                print("📂 Cargando desde caché...")
                return pickle.load(f)
        resultado = func(*args, **kwargs)
        with open(nombre, "wb") as f:
            pickle.dump(resultado, f)
        return resultado
    return wrapper

