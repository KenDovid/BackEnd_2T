// db.js
import pkg from 'pg';
const { Pool } = pkg;

export const pool = new Pool({
    host: 'localhost',
    user: 'postgres',
    password: 'Panda03010518',
    database: 'crud_express_pg',
    port: 5432
});


export default pool;