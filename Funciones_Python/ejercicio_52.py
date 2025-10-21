# 52. Contador con closure
def contador():
    total = 0
    def incrementar():
        nonlocal total
        total += 1
        return total
    return incrementar

