# 53. Closure que eleva a una potencia dada
def make_power(n):
    def elevar(x):
        return x ** n
    return elevar

