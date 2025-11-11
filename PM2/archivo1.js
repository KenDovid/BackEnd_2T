// Ejercicio 1: Suma de dos números con conversión.
const prompt = require('prompt-sync')({sigint: true});
// Solicitar números al usuario. 

// let numero1 = parseInt(prompt("Ingrese el primero número: "));
// let numero2 = parseInt(prompt("Ingrese el segundo número: "));

// let suma = numero1 + numero2;

// console.log(`La suma es ${suma}`)



// Versión con validación

let numero1 = parseInt(prompt("Ingrese el primero número: "));
let numero2 = parseInt(prompt("Ingrese el segundo número: "));

// Verificar conversión exitosa
if(isNaN(numero1) || isNaN(numero2)){
    console.log("Por favor ingrese números válidos");
} else {
    let resultado = numero1 + numero2;
    console.log(`El resultado de la suma es: ${resultado}`)
}