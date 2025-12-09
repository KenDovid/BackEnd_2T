import http from "http";

import { crearRegistro } from "./funcion_crear.js";
import { leerRegistro } from "./funcion_leer.js";
import { actualizarRegistro } from "./funcion_actualizar.js";
import { eliminarRegistro } from "./funcion_eliminar.js";

const PORT = 3000;

const server = http.createServer((req, res) => {
    res.setHeader("Content-Type", "application/json; charset=utf-8");

    if (req.url.startsWith("/create")) return crearRegistro(req, res);
    if (req.url.startsWith("/read")) return leerRegistro(req, res);
    if (req.url.startsWith("/update")) return actualizarRegistro(req, res);
    if (req.url.startsWith("/delete")) return eliminarRegistro(req, res);

    res.end(JSON.stringify({ error: "Ruta inválida" }));
});

server.listen(PORT, () => {
    console.log(`🟢 Servidor corriendo en http://localhost:${PORT}`);
});


// http://localhost:3000/create?name=Juan
// http://localhost:3000/read
// http://localhost:3000/update?id=12345&name=NuevoNombre
// http://localhost:3000/delete?id=12345