# 📱 Ejercicio 28: Encapsulación — Teléfono Inteligente
# Controla internamente el estado de encendido y batería.

class Telefono:
    def __init__(self):
        self.__encendido = False
        self.__bateria = 100

    def encender(self):
        if not self.__encendido:
            self.__encendido = True
            return "Teléfono encendido."
        return "Ya estaba encendido."

    def usar(self, minutos):
        if not self.__encendido:
            return "Debes encenderlo primero."
        if minutos * 2 > self.__bateria:
            return "Batería insuficiente."
        self.__bateria -= minutos * 2
        return f"Usaste el teléfono por {minutos} minutos. Batería: {self.__bateria}%"

# Uso
tel = Telefono()
print(tel.encender())
print(tel.usar(20))
