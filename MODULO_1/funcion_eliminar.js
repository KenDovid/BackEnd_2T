import { readData, writeData } from "./utils.js";

export function eliminarRegistro(req, res) {
    const url = new URL(req.url, `http://${req.headers.host}`);
    const id = Number(url.searchParams.get("id"));

    const data = readData();
    const newData = data.filter(item => item.id !== id);

    writeData(newData);

    console.log("📕 DELETE: ID =", id);
    res.end(JSON.stringify({ message: "Eliminado", id }));
}
