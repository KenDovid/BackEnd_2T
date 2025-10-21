# 🧰 Ejercicio 77: Manejo de Errores — Captura de Excepciones
# Usa try/except para manejar errores sin interrumpir el programa.

def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: división entre cero."

# Uso
print(dividir(10, 2))
print(dividir(10, 0))
