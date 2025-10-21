# 99. Pipeline de funciones
def data_pipeline(funcs, data):
    for f in funcs:
        data = f(data)
    return data

