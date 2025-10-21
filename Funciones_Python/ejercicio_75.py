# 75. Reintentar una función si lanza error
def retry(func, attempts=3):
    for intento in range(attempts):
        try:
            return func()
        except Exception as e:
            print(f"Intento {intento+1} fallido: {e}")
    print("Se agotaron los intentos.")
    return None

