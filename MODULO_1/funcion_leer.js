import { readData } from "./utils.js";

export function leerRegistro(req, res) {
    const data = readData();

    console.log("📘 READ:", data);
    res.end(JSON.stringify(data));
}
