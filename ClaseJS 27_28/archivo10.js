// Ejercicio push #1
let miArray = ['manzana', 'banana'];
miArray.push('naranja');
console.log(miArray); 

// Ejercicio push #2
let frutas = ['uva'];
frutas.push('fresa', 'kiwi', 'mango');
console.log(frutas); 

// Ejercicio push #3
let numeros = [1, 2];
let nuevaLongitud = numeros.push(3, 4);
console.log(numeros);       
console.log(nuevaLongitud); 

// Ejercicio push #4
let productos = ['libro', 'esfero'];
let nuevoProducto = { nombre: 'lápiz', precio: '1000' };
productos.push(nuevoProducto);
console.log(productos);

// Ejercicio push #5
let historial = [];
historial.push('Usuario inició sesión');
historial.push('Usuario vio su perfil');
historial.push('Usuario cerró sesión');
console.log(historial);
