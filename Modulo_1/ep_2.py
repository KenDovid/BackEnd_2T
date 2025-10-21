#Validador de contraseña

contraseña = input("Ingrese una contraseña: ")

if len(contraseña) >= 8 and any(c.isupper() for c in contraseña) and any(c.isdigit() for c in contraseña):
    print("Contraseña válida ✅")
else:
    print("Contraseña no válida ❌")
