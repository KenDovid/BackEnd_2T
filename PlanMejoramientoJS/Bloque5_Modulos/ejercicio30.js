function sumar(a,b){ return a + b; }
function sumarDoble(a,b){ return (a + b) * 2; }

const sumaSimple = sumar;
const sumaConMultiplicador = sumarDoble;

console.log("Suma simple:", sumaSimple(3,2));
console.log("Suma doble:", sumaConMultiplicador(5,5));
