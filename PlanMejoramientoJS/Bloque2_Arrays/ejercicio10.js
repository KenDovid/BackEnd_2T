function sumarArreglo(arr) {
  let suma = 0;
  for (let i = 0; i < arr.length; i++) {
    suma += arr[i];
  }
  return suma;
}

const ventas = [100, 200, 300, 400, 500];
console.log("Ventas:", ventas);
console.log("Total:", sumarArreglo(ventas));
