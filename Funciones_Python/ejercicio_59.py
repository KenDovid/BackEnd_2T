# 59. Demostrar diferencia entre reasignar lista y modificarla
def lista_demo():
    numeros = [1, 2, 3]
    def modificar(lst):
        lst.append(4)
    def reasignar(lst):
        lst = [9, 9, 9]
        return lst
    modificar(numeros)
    nueva = reasignar(numeros)
    return numeros, nueva

