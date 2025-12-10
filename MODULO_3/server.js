// server.js
import express from 'express';
import itemsRoutes from './routes/items.routes.js';
import pool from './db.js';
import exportRoutes from "./routes/export.js";
app.use("/api", exportRoutes);

const app = express();
app.use(express.json());

// Rutas del CRUD
app.use('/api', itemsRoutes);

// 🧪 Test de conexión a PostgreSQL
pool
  .connect()
  .then(() => console.log('🟢 Conexión a PostgreSQL exitosa'))
  .catch(err => console.error('🔴 Error al conectar a PostgreSQL:', err));

app.listen(3000, () => {
    console.log('🔥 Servidor corriendo en http://localhost:3000');
});
