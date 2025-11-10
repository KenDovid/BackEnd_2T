function esMayorDeEdad(edad) {
  if (typeof edad !== 'number') return false;
  return edad >= 18;
}

console.log("20 ->", esMayorDeEdad(20));
console.log("16 ->", esMayorDeEdad(16));
