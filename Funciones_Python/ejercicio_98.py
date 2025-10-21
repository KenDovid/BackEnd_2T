# 98. Cargar “plugins” desde archivos de carpeta (simulado)
def plugin_loader(path_to_dir):
    import os
    archivos = [f for f in os.listdir(path_to_dir) if f.endswith(".py")]
    print("Plugins detectados:", archivos)
    return archivos

