# 55. Acumulador con closure
def accumulator():
    total = 0
    def add(v):
        nonlocal total
        total += v
        return total
    return add

