# ⚙️ Ejercicio 55: Herencia Múltiple — Robot Multifunción
# Un robot combina habilidades de moverse, hablar y pensar.

class Movil:
    def mover(self):
        return "Me desplazo en el espacio."

class Comunicador:
    def hablar(self):
        return "Transmitiendo señal de voz."

class Inteligente:
    def pensar(self):
        return "Analizando datos y tomando decisiones."

class Robot(Movil, Comunicador, Inteligente):
    pass

# Uso
r2d2 = Robot()
print(r2d2.mover(), r2d2.hablar(), r2d2.pensar())
