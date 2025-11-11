// Ejercicio 14: Modificación Precisa con .splice()

let tareas  = [
    "Hacer cama", 
    "Comprar pan",
    "Estudiar JS",
    "Lavar platos"
];

console.log(`Inicial: ${tareas}`);

// splice(índice, cantidad_eliminar, nuevo_elemento)
tareas.splice(1,1, "Pasear al perro")

console.log(`Final ${tareas}`);