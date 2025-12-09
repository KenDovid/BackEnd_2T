import { readData, writeData } from "./utils.js";

export function actualizarRegistro(req, res) {
    const url = new URL(req.url, `http://${req.headers.host}`);
    const id = Number(url.searchParams.get("id"));
    const name = url.searchParams.get("name");

    const data = readData();
    const item = data.find(d => d.id === id);

    if (item) {
        const old = { ...item };
        item.name = name;
        writeData(data);

        console.log("📙 UPDATE:", { before: old, after: item });
    } else {
        console.log("⚠️ UPDATE FAILED: ID no encontrado:", id);
    }

    res.end(JSON.stringify({ message: "Actualizado", item }));
}
