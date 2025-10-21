# 💡 Ejercicio 37: Sistema de Notificaciones con Polimorfismo
# Cada tipo de notificación tiene su propia forma de enviar el mensaje.

class Notificacion:
    def enviar(self, mensaje):
        pass

class Email(Notificacion):
    def enviar(self, mensaje):
        return f"📧 Enviando correo: {mensaje}"

class SMS(Notificacion):
    def enviar(self, mensaje):
        return f"📱 Enviando SMS: {mensaje}"

class Push(Notificacion):
    def enviar(self, mensaje):
        return f"🔔 Enviando notificación push: {mensaje}"

# Uso
notifs = [Email(), SMS(), Push()]
for n in notifs:
    print(n.enviar("Hola Mundo"))
