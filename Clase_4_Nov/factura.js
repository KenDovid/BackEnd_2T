const fs = require('fs');
const readline = require('readline');

const FILE = 'facturas.txt';

// Crear interfaz de lectura
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Función para leer input de forma async
function pregunta(query) {
    return new Promise(resolve => rl.question(query, ans => resolve(ans)));
}

// Calcular subtotal, IVA y total
function calcularFactura(items) {
    let subtotal = 0;
    for (let item of items) {
        subtotal += item.cantidad * item.precio;
    }
    let iva = subtotal * 0.16;
    let total = subtotal + iva;
    return { subtotal, iva, total };
}

// Guardar factura en archivo
function guardarFactura(factura) {
    let facturas = [];
    if (fs.existsSync(FILE)) {
        const contenido = fs.readFileSync(FILE, 'utf-8');
        if (contenido) facturas = JSON.parse(contenido);
    }
    facturas.push(factura);
    fs.writeFileSync(FILE, JSON.stringify(facturas, null, 2));
}

// Imprimir factura bonita
function imprimirFactura(factura) {
    console.log('\n================ FACTURA ================');
    console.log(`ID: ${factura.id}`);
    console.log(`Cliente: ${factura.cliente}`);
    console.log('----------------------------------------');
    console.log('| Producto       | Cantidad | Precio | Total |');
    console.log('----------------------------------------');

    for (let item of factura.items) {
        const totalItem = item.cantidad * item.precio;
        console.log(`| ${item.nombre.padEnd(14)} | ${item.cantidad.toString().padStart(7)} | ${item.precio.toFixed(2).padStart(6)} | ${totalItem.toFixed(2).padStart(5)} |`);
    }

    console.log('----------------------------------------');
    console.log(`Subtotal: ${factura.subtotal.toFixed(2)}`);
    console.log(`IVA (16%): ${factura.iva.toFixed(2)}`);
    console.log(`Total: ${factura.total.toFixed(2)}`);
    console.log('========================================\n');
}

// Leer todas las facturas
function leerFacturas() {
    if (!fs.existsSync(FILE)) {
        console.log('No hay facturas.');
        return [];
    }
    const contenido = fs.readFileSync(FILE, 'utf-8');
    if (!contenido) {
        console.log('Archivo vacío.');
        return [];
    }
    const facturas = JSON.parse(contenido);
    facturas.forEach(f => imprimirFactura(f));
    return facturas;
}

// Crear factura interactiva
async function crearFactura() {
    const factura = {
        id: Date.now(),
        cliente: await pregunta('Ingrese el nombre del cliente: '),
        items: []
    };

    let agregar = 's';
    while (agregar.toLowerCase() === 's') {
        const nombre = await pregunta('Nombre del producto: ');
        const cantidad = parseFloat(await pregunta('Cantidad: '));
        const precio = parseFloat(await pregunta('Precio unitario: '));
        factura.items.push({ nombre, cantidad, precio });

        agregar = await pregunta('¿Agregar otro producto? (s/n): ');
    }

    const totals = calcularFactura(factura.items);
    factura.subtotal = totals.subtotal;
    factura.iva = totals.iva;
    factura.total = totals.total;

    guardarFactura(factura);
    console.log('Factura creada:');
    imprimirFactura(factura);
}

// Actualizar factura
async function actualizarFactura() {
    const facturas = leerFacturas();
    if (facturas.length === 0) return;

    const id = await pregunta('Ingrese el ID de la factura a actualizar: ');
    const factura = facturas.find(f => f.id.toString() === id);
    if (!factura) {
        console.log('Factura no encontrada.');
        return;
    }

    factura.cliente = await pregunta(`Cliente actual (${factura.cliente}): `) || factura.cliente;

    for (let i = 0; i < factura.items.length; i++) {
        const item = factura.items[i];
        const nombre = await pregunta(`Producto ${i + 1} actual (${item.nombre}): `);
        const cantidad = await pregunta(`Cantidad actual (${item.cantidad}): `);
        const precio = await pregunta(`Precio actual (${item.precio}): `);

        if (nombre) item.nombre = nombre;
        if (cantidad) item.cantidad = parseFloat(cantidad);
        if (precio) item.precio = parseFloat(precio);
    }

    const totals = calcularFactura(factura.items);
    factura.subtotal = totals.subtotal;
    factura.iva = totals.iva;
    factura.total = totals.total;

    fs.writeFileSync(FILE, JSON.stringify(facturas, null, 2));
    console.log('Factura actualizada:');
    imprimirFactura(factura);
}

// Eliminar factura
async function eliminarFactura() {
    const facturas = leerFacturas();
    if (facturas.length === 0) return;

    const id = await pregunta('Ingrese el ID de la factura a eliminar: ');
    const index = facturas.findIndex(f => f.id.toString() === id);
    if (index === -1) {
        console.log('Factura no encontrada.');
        return;
    }

    const eliminada = facturas.splice(index, 1)[0];
    fs.writeFileSync(FILE, JSON.stringify(facturas, null, 2));
    console.log('Factura eliminada:');
    imprimirFactura(eliminada);
}

// Menú interactivo
async function menu() {
    let opcion = '';
    do {
        console.log('\n--- MENÚ DE FACTURAS ---');
        console.log('1. Crear factura');
        console.log('2. Leer facturas');
        console.log('3. Actualizar factura');
        console.log('4. Eliminar factura');
        console.log('5. Salir');
        opcion = await pregunta('Seleccione una opción: ');

        switch (opcion) {
            case '1':
                await crearFactura();
                break;
            case '2':
                leerFacturas();
                break;
            case '3':
                await actualizarFactura();
                break;
            case '4':
                await eliminarFactura();
                break;
            case '5':
                console.log('Saliendo...');
                break;
            default:
                console.log('Opción no válida.');
        }
    } while (opcion !== '5');

    rl.close();
}

// Ejecutar menú
menu();
