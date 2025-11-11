// Ejercicio 9 Suma de Elementos con Bucle.

function sumarArreglo(arr){
    let suma = 0;
    for (let i = 0; i < arr.length; i++){
        suma += arr[i]
    }
    return suma
}

let ventas = [100, 200, 300, 400, 500];
console.log(`Total ${sumarArreglo(ventas)}`);
