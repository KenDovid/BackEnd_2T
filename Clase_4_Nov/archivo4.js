const fs = require('fs');
const archivo_datos = "datos.txt";

fs.readFile(archivo_datos, 'utf8', (error, datos) => {
    if(error){
        console.error("Error al leer: ", error);
    }
    const nuevoContenido = datos + new Date().toLocaleString();
    fs.writeFile(archivo_datos, nuevoContenido, (error) =>{
        if(error){
            console.error("Error al guardar", error);
        } else {
            console.log("Archivo editado");
        }
    });
});