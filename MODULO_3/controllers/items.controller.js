// controllers/items.controller.js
import { pool } from '../db.js';

export const getItems = async (req, res) => {
    const result = await pool.query('SELECT * FROM items ORDER BY id ASC');
    res.json(result.rows);
};

export const createItem = async (req, res) => {
    const { name } = req.body;
    const result = await pool.query(
        'INSERT INTO items (name) VALUES ($1) RETURNING *',
        [name]
    );
    res.json(result.rows[0]);
};

export const updateItem = async (req, res) => {
    const { id } = req.params;
    const { name } = req.body;

    const result = await pool.query(
        'UPDATE items SET name = $1 WHERE id = $2 RETURNING *',
        [name, id]
    );

    res.json(result.rows[0]);
};

export const deleteItem = async (req, res) => {
    const { id } = req.params;

    await pool.query('DELETE FROM items WHERE id = $1', [id]);
    res.json({ message: 'Item eliminado' });
};
