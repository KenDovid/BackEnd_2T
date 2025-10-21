# 51. Variable local vs global
x = 10
def demo_scope():
    x = 5  # variable local
    print("Dentro de la función:", x)
print("Fuera de la función:", x)

