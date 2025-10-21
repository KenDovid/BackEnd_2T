# 💡 Ejercicio 73: Patrón Observer — Sistema de Notificaciones
# Varios objetos observan a otro y reaccionan cuando algo cambia.

class Sujeto:
    def __init__(self):
        self.observadores = []

    def agregar(self, obs):
        self.observadores.append(obs)

    def notificar(self, mensaje):
        for o in self.observadores:
            o.actualizar(mensaje)

class Observador:
    def actualizar(self, mensaje):
        print(f"Notificación recibida: {mensaje}")

# Uso
sujeto = Sujeto()
obs1, obs2 = Observador(), Observador()
sujeto.agregar(obs1)
sujeto.agregar(obs2)
sujeto.notificar("El sistema ha sido actualizado.")
