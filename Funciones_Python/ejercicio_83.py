# 83. Decorador de memoización para acelerar funciones recursivas
def memoize_decorator(func):
    cache = {}
    def wrapper(x):
        if x not in cache:
            cache[x] = func(x)
        return cache[x]
    return wrapper

# Ejemplo de uso con Fibonacci
@memoize_decorator
def fib_memo(n):
    if n <= 1:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)

