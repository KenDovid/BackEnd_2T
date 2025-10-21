# 33. Enmascarar correo electrónico
def mask_email(email):
    parte_usuario, dominio = email.split("@")
    if len(parte_usuario) > 2:
        parte_usuario = parte_usuario[:2] + "***"
    else:
        parte_usuario = parte_usuario[0] + "***"
    return parte_usuario + "@" + dominio

