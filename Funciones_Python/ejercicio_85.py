# 85. Decorador con parámetros (reintentos)
def retry_decorator(attempts=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for intento in range(attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Error: {e}, intento {intento + 1} de {attempts}")
            print("❌ Falló después de varios intentos.")
        return wrapper
    return decorator

