# 79. Registrar y relanzar excepciones
def log_and_raise():
    try:
        1 / 0
    except Exception as e:
        print(f"Error registrado: {e}")
        raise  # vuelve a lanzar el error

