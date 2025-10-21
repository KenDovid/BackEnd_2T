# 56. Closure que registra cantidad de llamadas
def registro_llamadas():
    contador = 0
    def llamada():
        nonlocal contador
        contador += 1
        print(f"Llamada número: {contador}")
    return llamada

