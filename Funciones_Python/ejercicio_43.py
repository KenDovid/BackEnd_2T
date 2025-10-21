# 43. Componer funciones f(g(x))
def compose(f, g):
    return lambda x: f(g(x))

