const fs = require('fs');
try {
  if (fs.existsSync('datos_ej31.txt')) {
    fs.unlinkSync('datos_ej31.txt');
    console.log("Archivo 'datos_ej31.txt' eliminado.");
  } else {
    console.log("Archivo no existe, nada que eliminar.");
  }
} catch (err) {
  console.log("Error al eliminar archivo:", err.message);
}
