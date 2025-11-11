// Ejercicio 10: Filtrado con .filter()

let temperaturas = [15, 22, 33, 45, 68, 82, 91];

let temperaturasAltas = temperaturas.filter(temp =>  temp > 50);

console.log(`Originales: ${temperaturas}`);
console.log(`Mayores a 50: ${temperaturasAltas}`);

