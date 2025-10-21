# 💾 Ejercicio 53: Mixin con Fecha — Seguimiento de Creación
# Añade a cualquier clase la capacidad de registrar su fecha de creación.

from datetime import datetime

class CreacionMixin:
    def __init__(self):
        self.fecha_creacion = datetime.now()

class Documento(CreacionMixin):
    def __init__(self, titulo):
        super().__init__()
        self.titulo = titulo

# Uso
doc = Documento("Informe Python")
print(f"{doc.titulo} creado el {doc.fecha_creacion}")
