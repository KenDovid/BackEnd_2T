# 🧩 Ejercicio 100: Proyecto Final — Sistema de Gestión General
# Combina conceptos: usuarios, roles y acciones. Un cierre integral.

class Usuario:
    def __init__(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol
        self.acciones = []

    def realizar_accion(self, accion):
        self.acciones.append(accion)
        return f"{self.nombre} realizó la acción: {accion}"

class Rol:
    def __init__(self, nombre, permisos):
        self.nombre = nombre
        self.permisos = permisos

class Sistema:
    def __init__(self):
        self.usuarios = []

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def mostrar_usuarios(self):
        return [u.nombre for u in self.usuarios]

# Uso
admin = Rol("Administrador", ["crear", "editar", "eliminar"])
usuario = Usuario("Lucía", admin)
sistema = Sistema()
sistema.agregar_usuario(usuario)
print(usuario.realizar_accion("crear"))
print("Usuarios registrados:", sistema.mostrar_usuarios())
