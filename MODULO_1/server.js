import http from "http";
import fs from "fs";

const PORT = 3000;
const FILE = "data.json";

// Función para leer JSON
function readData() {
    try {
        let fileContent = fs.readFileSync(FILE, "utf8");
        return JSON.parse(fileContent);
    } catch (err) {
        return [];
    }
}

// Función para escribir JSON
function writeData(data) {
    fs.writeFileSync(FILE, JSON.stringify(data, null, 2), "utf8");
}

const server = http.createServer((req, res) => {
    res.setHeader("Content-Type", "application/json; charset=utf-8");

    // ---- CREATE ----
    if (req.url.startsWith("/create")) {
        const url = new URL(req.url, `http://${req.headers.host}`);
        const name = url.searchParams.get("name");

        const data = readData();
        const newItem = { id: Date.now(), name };
        data.push(newItem);
        writeData(data);

        console.log("📗 CREATE:", newItem); // ← Log para consola

        res.end(JSON.stringify({ message: "Creado", item: newItem }));
        return;
    }

    // ---- READ ----
    if (req.url.startsWith("/read")) {
        const data = readData();

        console.log("📘 READ:", data); // ← Log

        res.end(JSON.stringify(data));
        return;
    }

    // ---- UPDATE ----
    if (req.url.startsWith("/update")) {
        const url = new URL(req.url, `http://${req.headers.host}`);
        const id = Number(url.searchParams.get("id"));
        const name = url.searchParams.get("name");

        const data = readData();
        const item = data.find(d => d.id === id);

        if (item) {
            const old = { ...item };
            item.name = name;
            writeData(data);

            console.log("📙 UPDATE:", { before: old, after: item }); // ← Log
        } else {
            console.log("⚠️ UPDATE FAILED: ID no encontrado:", id);
        }

        res.end(JSON.stringify({ message: "Actualizado", item }));
        return;
    }

    // ---- DELETE ----
    if (req.url.startsWith("/delete")) {
        const url = new URL(req.url, `http://${req.headers.host}`);
        const id = Number(url.searchParams.get("id"));

        let data = readData();
        const newData = data.filter(item => item.id !== id);

        writeData(newData);

        console.log("📕 DELETE: ID =", id); // ← Log

        res.end(JSON.stringify({ message: "Eliminado", id }));
        return;
    }

    res.end(JSON.stringify({ error: "Ruta inválida" }));
});

server.listen(PORT, () => {
    console.log(`🟢 Servidor corriendo en http://localhost:${PORT}`);
});


// ======================================================
// COMANDOS PARA PROBAR EL CRUD DESDE EL NAVEGADOR
// ======================================================

// 🟢 CREATE (crear un registro)
// http://localhost:3000/create?name=TuNombre

// 🔵 READ (leer todos los registros)
// http://localhost:3000/read

// 🟡 UPDATE (actualizar un registro por ID)
// http://localhost:3000/update?id=ID_A_CAMBIAR&name=NuevoNombre

// 🔴 DELETE (eliminar un registro por ID)
// http://localhost:3000/delete?id=ID_A_ELIMINAR
