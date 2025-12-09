import fs from "fs";

const FILE = "data.json";

export function readData() {
    try {
        const fileContent = fs.readFileSync(FILE, "utf8");
        return JSON.parse(fileContent);
    } catch (err) {
        return [];
    }
}

export function writeData(data) {
    fs.writeFileSync(FILE, JSON.stringify(data, null, 2), "utf8");
}
