# 74. Validar formato básico de correo electrónico
def validate_email(email):
    if "@" not in email or "." not in email.split("@")[-1]:
        raise ValueError("Correo inválido")
    return True

