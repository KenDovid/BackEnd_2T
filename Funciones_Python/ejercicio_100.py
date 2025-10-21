# 100. Mini suite de pruebas
def mini_test_suite(funcs_with_tests):
    exitos, fallos = 0, 0
    for func, test_func in funcs_with_tests:
        try:
            test_func(func)
            exitos += 1
        except AssertionError:
            print(f"❌ Falló la prueba de {func.__name__}")
            fallos += 1
    print(f"✅ {exitos} pasaron | ❌ {fallos} fallaron")
