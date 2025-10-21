#Sistema de recomendación

gusto = input("¿Qué te gusta? (cine, música, lectura): ").lower()

if gusto == "cine":
    print("Te recomiendo ver 'Inception'.")
elif gusto == "música":
    print("Escucha 'Bohemian Rhapsody' de Queen.")
elif gusto == "lectura":
    print("Lee '1984' de George Orwell.")
else:
    print("¡Explora nuevos intereses!")
