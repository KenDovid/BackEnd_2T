# 81. Decorador que mide el tiempo de ejecución
import time

def timing(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"⏱️ Tiempo: {fin - inicio:.5f} segundos")
        return resultado
    return wrapper

