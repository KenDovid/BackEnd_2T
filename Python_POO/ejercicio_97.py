# 🧠 Ejercicio 97: Sistema de Login Simulado
# Verifica usuarios con validación básica.

class Usuario:
    def __init__(self, nombre, password):
        self.nombre = nombre
        self.password = password

class SistemaLogin:
    def __init__(self):
        self.usuarios = []

    def registrar(self, usuario):
        self.usuarios.append(usuario)

    def autenticar(self, nombre, password):
        for u in self.usuarios:
            if u.nombre == nombre and u.password == password:
                return "Acceso concedido."
        return "Credenciales incorrectas."

# Uso
s = SistemaLogin()
s.registrar(Usuario("admin", "1234"))
print(s.autenticar("admin", "1234"))
