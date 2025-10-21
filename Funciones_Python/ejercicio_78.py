# 78. Simular función que lanza TimeoutError
def timeout_demo(segundos):
    import time
    if segundos > 5:
        raise TimeoutError("Se superó el tiempo límite.")
    time.sleep(segundos)
    return "Completado a tiempo"

