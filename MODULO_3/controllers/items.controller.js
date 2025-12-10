// controllers/items.controller.js
import { pool } from "../db.js";

export const getItems = async (req, res) => {
    const result = await pool.query("SELECT * FROM items ORDER BY id ASC");
    res.json(result.rows);
};

export const getItem = async (req, res) => {
    const result = await pool.query(
        "SELECT * FROM items WHERE id = $1",
        [req.params.id]
    );

    if (result.rows.length === 0)
        return res.status(404).json({ message: "Item no encontrado" });

    res.json(result.rows[0]);
};

export const createItem = async (req, res) => {
    const { name, descripcion, valor } = req.body;

    const result = await pool.query(
        "INSERT INTO items (name, descripcion, valor) VALUES ($1, $2, $3) RETURNING *",
        [name, descripcion, valor]
    );

    res.status(201).json(result.rows[0]);
};

export const updateItem = async (req, res) => {
    const { name, descripcion, valor } = req.body;

    const result = await pool.query(
        "UPDATE items SET name=$1, descripcion=$2, valor=$3 WHERE id=$4 RETURNING *",
        [name, descripcion, valor, req.params.id]
    );

    if (result.rows.length === 0)
        return res.status(404).json({ message: "Item no encontrado" });

    res.json(result.rows[0]);
};

export const patchItem = async (req, res) => {
    const { id } = req.params;
    const fields = [];
    const values = [];
    let index = 1;

    for (const key in req.body) {
        fields.push(`${key} = $${index}`);
        values.push(req.body[key]);
        index++;
    }

    values.push(id);

    const query = `UPDATE items SET ${fields.join(", ")} WHERE id = $${index} RETURNING *`;

    const result = await pool.query(query, values);

    if (result.rows.length === 0)
        return res.status(404).json({ message: "Item no encontrado" });

    res.json(result.rows[0]);
};

export const deleteItem = async (req, res) => {
    const result = await pool.query(
        "DELETE FROM items WHERE id = $1 RETURNING *",
        [req.params.id]
    );

    if (result.rows.length === 0)
        return res.status(404).json({ message: "Item no encontrado" });

    res.json({ message: "Item eliminado" });
};
