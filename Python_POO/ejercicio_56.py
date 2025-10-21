# 🧱 Ejercicio 56: Composición + Herencia — Edificio con Energía
# Combina herencia (Edificio → Hospital) y composición (con un Generador).

class Generador:
    def __init__(self, potencia):
        self.potencia = potencia

    def encender(self):
        return f"Generador encendido ({self.potencia} kW)."

class Edificio:
    def __init__(self, nombre):
        self.nombre = nombre

class Hospital(Edificio):
    def __init__(self, nombre, generador):
        super().__init__(nombre)
        self.generador = generador

    def iniciar_emergencia(self):
        return f"{self.nombre}: {self.generador.encender()}"

# Uso
gen = Generador(500)
hospital = Hospital("Clínica Esperanza", gen)
print(hospital.iniciar_emergencia())
