const fs = require('fs');
const nuevaLinea = "\nAñadido por ejercicio33_update.js";
try {
  fs.appendFileSync('datos_ej31.txt', nuevaLinea, 'utf8');
  console.log("Se añadió una línea a 'datos_ej31.txt'");
} catch (err) {
  console.log("Error al actualizar archivo:", err.message);
}
