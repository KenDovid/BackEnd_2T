// ejercicio18.js
const verificarAcceso = (edad) => edad >= 18 ? "Permitido" : "Denegado";

console.log("17 años:", verificarAcceso(17));
// "Denegado"

console.log("35 años:", verificarAcceso(35));
// "Permitido"