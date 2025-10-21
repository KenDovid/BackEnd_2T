# 🧩 Ejercicio 54: Herencia Múltiple con Conflictos (Orden MRO)
# Muestra cómo Python resuelve el orden de herencia con super().

class A:
    def mensaje(self):
        return "Clase A"

class B(A):
    def mensaje(self):
        return "Clase B → " + super().mensaje()

class C(A):
    def mensaje(self):
        return "Clase C → " + super().mensaje()

class D(B, C):
    def mensaje(self):
        return "Clase D → " + super().mensaje()

# Uso
obj = D()
print(obj.mensaje())
print(D.__mro__)  # Orden de resolución de métodos
