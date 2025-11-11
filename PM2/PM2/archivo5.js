// Ejercicio 5: Calculadora de impuestos
const prompt = require('prompt-sync')({ sigint: true });

const TASA_IMPUESTO = 0.15;

let precio = Number(prompt("Ingrese el precio: "));


if (!isNaN(precio)) {
    let impuesto = precio * TASA_IMPUESTO;
    let total = precio + impuesto;

    console.log(`Precio base: ${precio}.`)
    console.log(`Impuesto (15%): ${impuesto.toFixed(2)}`);
    console.log(`Total a pagar: ${total.toFixed(2)}`)
} else{
    console.log("Error: Entrada inválida.")
}