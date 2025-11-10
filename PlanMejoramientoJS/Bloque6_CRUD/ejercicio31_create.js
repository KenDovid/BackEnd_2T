const fs = require('fs');
const contenido = "Linea inicial\nEste archivo fue creado por ejercicio31_create.js";
fs.writeFileSync('datos_ej31.txt', contenido, 'utf8');
console.log("Archivo 'datos_ej31.txt' creado con contenido inicial.");
