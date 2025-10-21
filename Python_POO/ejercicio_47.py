# ⚙️ Ejercicio 47: Composición — Auto con Motor
# Una clase contiene otra clase como atributo.

class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

    def encender(self):
        return "Motor encendido."

class Auto:
    def __init__(self, marca, motor):
        self.marca = marca
        self.motor = motor

    def iniciar(self):
        return f"{self.marca}: {self.motor.encender()}"

# Uso
motor = Motor(2000)
auto = Auto("Toyota", motor)
print(auto.iniciar())
