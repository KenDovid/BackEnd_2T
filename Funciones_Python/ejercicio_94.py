# 94. Calculadora CLI simple
def mini_cli_calc():
    while True:
        operacion = input("Operación (ej: 2 + 2) o 'salir': ")
        if operacion.lower() == "salir":
            break
        try:
            print("Resultado:", eval(operacion))
        except Exception as e:
            print("Error:", e)

