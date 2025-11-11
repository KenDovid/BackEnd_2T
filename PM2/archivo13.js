// Ejercicio 13: Transformación con .map()

let preciosBase = [100, 250, 399, 75];
let preciosConAumento = preciosBase.map(precio => precio * 1.10);

console.log(`Originales: ${preciosBase}`);
console.log(`Con 10% de descuento: ${preciosConAumento}`)