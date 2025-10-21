# 🧰 Ejercicio 23: Encapsulación Avanzada — Temperatura con Validación
# Controla la lectura y modificación de una temperatura con validaciones.

class Termometro:
    def __init__(self, celsius=0):
        self.__celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, valor):
        if -273.15 <= valor <= 1000:
            self.__celsius = valor
        else:
            raise ValueError("Temperatura fuera de rango físico.")

    @property
    def fahrenheit(self):
        return (self.__celsius * 9/5) + 32

# Uso
t = Termometro(25)
print(f"{t.celsius}°C = {t.fahrenheit}°F")
t.celsius = 100
print(f"{t.celsius}°C = {t.fahrenheit}°F")
