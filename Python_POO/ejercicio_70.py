# ⚙️ Ejercicio 70: Decorador de Clase Avanzado — Añadir Método Dinámicamente
# Un decorador que inserta un nuevo método en una clase.

def agregar_metodo_saludo(cls):
    def saludar(self):
        return f"Hola desde {cls.__name__}!"
    cls.saludar = saludar
    return cls

@agregar_metodo_saludo
class Servicio:
    pass

# Uso
s = Servicio()
print(s.saludar())
