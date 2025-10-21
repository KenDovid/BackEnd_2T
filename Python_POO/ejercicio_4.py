# 🚗 Ejercicio 4: Clase Vehículo
# Crea una clase con métodos para acelerar, frenar y consultar la velocidad.

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0

    def acelerar(self, incremento):
        if incremento > 0:
            self.velocidad += incremento
            return f"{self.marca} {self.modelo} acelera a {self.velocidad} km/h."
        return "Incremento inválido."

    def frenar(self, decremento):
        self.velocidad = max(0, self.velocidad - decremento)
        return f"{self.marca} {self.modelo} frena a {self.velocidad} km/h."

# Uso
auto = Vehiculo("Toyota", "Corolla")
print(auto.acelerar(50))
print(auto.frenar(20))
