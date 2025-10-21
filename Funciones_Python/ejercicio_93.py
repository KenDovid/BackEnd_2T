# 93. App de tareas en consola (simulada)
def todo_app():
    tareas = []
    while True:
        accion = input("Agregar (a), Mostrar (m), Salir (s): ").lower()
        if accion == 'a':
            tarea = input("Nueva tarea: ")
            tareas.append(tarea)
        elif accion == 'm':
            for i, t in enumerate(tareas, 1):
                print(f"{i}. {t}")
        elif accion == 's':
            break
    return tareas

