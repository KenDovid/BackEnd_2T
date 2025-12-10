import PDFDocument from "pdfkit";
import fs from "fs";
import path from "path";
import { pool } from "./db.js";

// Crear carpeta tmp si no existe
const tmpPath = path.join(process.cwd(), "tmp");
if (!fs.existsSync(tmpPath)) {
    fs.mkdirSync(tmpPath);
}

async function generatePDF() {
    try {
        console.log("🎨 Generando PDF...");

        // Consultar la base de datos
        const result = await pool.query("SELECT id, name, descripcion, valor FROM items ORDER BY id ASC");

        // Crear nombre único
        const filename = `reporte_${Date.now()}.pdf`;
        const filePath = path.join(tmpPath, filename);

        // Crear documento PDF
        const doc = new PDFDocument({ margin: 40 });
        const stream = fs.createWriteStream(filePath);
        doc.pipe(stream);

        // Título
        doc.fontSize(22).text("Reporte de Items", { align: "center" });
        doc.moveDown();

        // Fecha
        const fecha = new Date().toLocaleString("es-CO");
        doc.fontSize(10).text(`Generado el: ${fecha}`);
        doc.moveDown();

        // Encabezados
        doc.fontSize(14).text("ID | Nombre | Descripción | Valor");
        doc.moveDown(0.5);

        // Datos
        result.rows.forEach((item) => {
            doc.fontSize(12).text(
                `${item.id} | ${item.name} | ${item.descripcion} | $${item.valor}`
            );
        });

        // Finalizar
        doc.end();

        // Esperar a que termine de guardarse
        stream.on("finish", () => {
            console.log(`✅ PDF generado con éxito: ${filePath}`);
        });

    } catch (error) {
        console.error("❌ Error generando PDF:", error);
    }
}

// Ejecutar si se llama directamente
generatePDF();
