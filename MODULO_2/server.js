import express from "express";
import fs from "fs";

const app = express();
const PORT = 3000;

app.use(express.static("public"));

const FILE = "data.json";

// =========================
// Funciones helper
// =========================
function readData() {
    if (!fs.existsSync(FILE)) return [];
    return JSON.parse(fs.readFileSync(FILE, "utf8"));
}

function writeData(data) {
    fs.writeFileSync(FILE, JSON.stringify(data, null, 2), "utf8");
}

// =========================
// RUTA INICIO
// =========================
app.get("/", (req, res) => {
    res.send(`
    <h1>CRUD con Express</h1>
    <p>Rutas disponibles:</p>
    <ul>
      <li>GET /items</li>
      <li>GET /create?name=TuNombre</li>
      <li>GET /update?id=1&name=NuevoNombre</li>
      <li>GET /delete?id=1</li>
    </ul>
  `);
});

// =========================
// READ
// =========================
app.get("/items", (req, res) => {
    res.json(readData());
});

// =========================
// CREATE
// =========================
app.get("/create", (req, res) => {
    const name = req.query.name;

    if (!name) {
        return res.send("Falta el parámetro name");
    }

    const data = readData();
    const newItem = { id: Date.now(), name };

    data.push(newItem);
    writeData(data);

    res.send(`Registro creado: ${JSON.stringify(newItem)}`);
});

// =========================
// UPDATE (CORREGIDO)
// =========================
app.get("/update", (req, res) => {
    const id = Number(req.query.id);
    const name = req.query.name?.trim();

    // Validación correcta
    if (isNaN(id) || !name) {
        return res.send("Faltan parámetros válidos: id y name");
    }

    const data = readData();
    const item = data.find(item => item.id === id);

    if (!item) {
        return res.send("ID no encontrado");
    }

    item.name = name;
    writeData(data);

    res.send(`Registro actualizado: ${JSON.stringify(item)}`);
});

// =========================
// DELETE
// =========================
app.get("/delete", (req, res) => {
    const id = Number(req.query.id);

    if (isNaN(id)) {
        return res.send("Parámetro id inválido o faltante");
    }

    const data = readData();
    const newData = data.filter(item => item.id !== id);

    if (newData.length === data.length) {
        return res.send("ID no encontrado");
    }

    writeData(newData);

    res.send(`Registro eliminado con id: ${id}`);
});

// =========================
// INICIAR SERVIDOR
// =========================
app.listen(PORT, () => {
    console.log(`🔥 Servidor listo en http://localhost:${PORT}`);
});
