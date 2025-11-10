let pilaLibros = ["El Quijote", "100 Años de Soledad", "Fahrenheit 451"];
console.log("Inicial (length):", pilaLibros.length);

// push -> agregar al final
pilaLibros.push("Moby Dick");
console.log("Después de push (length):", pilaLibros.length);

// pop -> remover último
const libroEliminado = pilaLibros.pop();
console.log("Libro eliminado:", libroEliminado);
console.log("Array final:", pilaLibros);
