// Ejercicio 9: Manipulación Básica de Arrays. 

let pilaLibros = ["El quijote", "100 Años de soledad", "Fahrenheit 451"];

console.log(`Libros inicales: ${pilaLibros.length}`);

// Agrega al final
pilaLibros.push("Moby Dick");
console.log(`Después de push: ${pilaLibros.length}`);
console.log(`Libros: ${pilaLibros}`);

// Remover del final
let libroEliminado = pilaLibros.pop();
console.log(`Libro removido ${libroEliminado}`);
console.log(`Libros finales: ${pilaLibros.length}`);