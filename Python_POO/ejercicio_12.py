# 🚘 Ejercicio 12: Clase Vehículo y Subclases Auto/Moto
# Practica herencia múltiple y sobreescritura de métodos.

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0

    def acelerar(self, incremento):
        self.velocidad += incremento
        return f"{self.marca} {self.modelo} acelera a {self.velocidad} km/h."

    def frenar(self, decremento):
        self.velocidad = max(0, self.velocidad - decremento)
        return f"{self.marca} {self.modelo} frena a {self.velocidad} km/h."

class Auto(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def abrir_puertas(self):
        return f"El {self.marca} {self.modelo} abre sus {self.puertas} puertas."

    def acelerar(self, incremento):
        self.velocidad += incremento * 1.2
        return f"El Auto {self.marca} rugió a {self.velocidad} km/h."

class Moto(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def hacer_caballito(self):
        return f"La Moto {self.marca} está haciendo un caballito."

    def acelerar(self, incremento):
        self.velocidad += incremento * 1.5
        return f"La Moto {self.marca} se lanzó a {self.velocidad} km/h."

# Uso
auto = Auto("Toyota", "Corolla", 4)
moto = Moto("Honda", "CBR500R", "Deportiva")
print(auto.acelerar(30))
print(moto.hacer_caballito())
