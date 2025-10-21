# 72. Factorial con aserción para evitar negativos
def factorial_check(n):
    assert n >= 0, "El número debe ser no negativo"
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

