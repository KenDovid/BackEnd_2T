import { readData, writeData } from "./utils.js";

export function crearRegistro(req, res) {
    const url = new URL(req.url, `http://${req.headers.host}`);
    const name = url.searchParams.get("name");

    const data = readData();
    const newItem = { id: Date.now(), name };
    data.push(newItem);
    writeData(data);

    console.log("📗 CREATE:", newItem);
    res.end(JSON.stringify({ message: "Creado", item: newItem }));
}
