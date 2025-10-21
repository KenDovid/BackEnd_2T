# 88. Decorador que cuenta cuántas veces se llamó a la función
def profile_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"Llamada #{wrapper.calls} a {func.__name__}")
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

