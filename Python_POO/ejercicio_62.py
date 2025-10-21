# ⚙️ Ejercicio 62: Decorador de Clase para Medir Tiempo
# Mide el tiempo de ejecución de los métodos dentro de una clase.

import time

def medir_tiempo(cls):
    class NuevaClase(cls):
        def ejecutar(self, *args, **kwargs):
            inicio = time.time()
            resultado = super().ejecutar(*args, **kwargs)
            duracion = time.time() - inicio
            print(f"⏱️ Tiempo: {duracion:.4f} segundos")
            return resultado
    return NuevaClase

@medir_tiempo
class Tarea:
    def ejecutar(self):
        time.sleep(0.3)
        return "Tarea completada."

# Uso
t = Tarea()
print(t.ejecutar())
