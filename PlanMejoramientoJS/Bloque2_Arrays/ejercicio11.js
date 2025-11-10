const temperaturas = [15, 22, 33, 45, 68, 82, 91];
const temperaturasAltas = temperaturas.filter(temp => temp > 50);
console.log("Original:", temperaturas);
console.log("Mayores a 50:", temperaturasAltas);
