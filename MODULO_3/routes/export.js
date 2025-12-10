import express from "express";
import PDFDocument from "pdfkit";
import path from "path";
import { pool } from "../db.js";

const router = express.Router();

router.get("/export", async (req, res) => {
    try {
        const result = await pool.query("SELECT id, name, descripcion, valor FROM items ORDER BY id ASC");

        const doc = new PDFDocument();
        const filename = `reporte_${Date.now()}.pdf`;

        // Configurar headers
        res.setHeader("Content-Type", "application/pdf");
        res.setHeader("Content-Disposition", `attachment; filename=${filename}`);

        // Enviar PDF al cliente directo por stream
        doc.pipe(res);

        // Título
        doc.fontSize(22).text("Reporte de Items", { align: "center" });
        doc.moveDown();

        // Fecha
        const fecha = new Date().toLocaleString("es-CO");
        doc.fontSize(10).text(`Generado el: ${fecha}`);
        doc.moveDown();

        // Encabezados
        doc.fontSize(14).text("ID | Nombre | Descripción | Valor");
        doc.moveDown();

        // Filas
        result.rows.forEach(item => {
            doc.fontSize(12).text(
                `${item.id} | ${item.name} | ${item.descripcion} | $${item.valor}`
            );
        });

        doc.end();

    } catch (err) {
        console.error(err);
        res.status(500).json({ error: "Error generando PDF" });
    }
});

export default router;
