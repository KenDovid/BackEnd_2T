# 82. Decorador que verifica autenticación
user_authenticated = True

def authenticated(func):
    def wrapper(*args, **kwargs):
        if user_authenticated:
            return func(*args, **kwargs)
        else:
            print("🚫 Acceso denegado. Usuario no autenticado.")
    return wrapper

