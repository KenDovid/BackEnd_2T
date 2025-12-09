// server.js
import express from 'express';
import itemsRoutes from './routes/items.routes.js';

const app = express();
app.use(express.json());

// Rutas del CRUD
app.use('/api', itemsRoutes);

app.listen(3000, () => {
    console.log('🔥 Servidor corriendo en http://localhost:3000');
});
