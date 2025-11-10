const VERSION = "1.0.0";
function saludarUsuario(nombre) {
  return `Hola ${nombre}. Versión: ${VERSION}`;
}

console.log("VERSION:", VERSION);
console.log(saludo => saludarUsuario("Ana"));
console.log(saludarUsuario("Ana"));
