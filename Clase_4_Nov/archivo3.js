const fs = require('fs');
const archivo_datos = "datos.txt";

fs.readfile(archivo_datos,  'utf8',
    (err,data) => {
        console.log(data);
    }
)