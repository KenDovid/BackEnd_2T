const fs = require('fs');
try {
  const data = fs.readFileSync('datos_ej31.txt', 'utf8');
  console.log("Contenido de 'datos_ej31.txt':\n", data);
} catch (err) {
  console.log("Error leyendo archivo (¿ejercicio31_create.js fue ejecutado?):", err.message);
}
