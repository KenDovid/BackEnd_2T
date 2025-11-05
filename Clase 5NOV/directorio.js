function iniciarDirectorio(callback) {
    const fs = require('fs');
    const readline = require('readline');
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    let contactos = [];

    function pedirContacto() {
        rl.question('Ingrese el nombre del contacto: ', (nombre) => {
            rl.question('Ingrese el teléfono: ', (telefono) => {
                contactos.push({ nombre, telefono });

                rl.question('¿Desea agregar otro contacto? (s/n): ', (respuesta) => {
                    if (respuesta.toLowerCase() === 's') {
                        pedirContacto();
                    } else {
                        guardarArchivo();
                    }
                });
            });
        });
    }

    function guardarArchivo() {
        const contenido = contactos
            .map(c => `Nombre: ${c.nombre}, Teléfono: ${c.telefono}`)
            .join('\n');

        fs.writeFile('agenda.txt', contenido, (err) => {
            if (err) console.error('Error al crear el archivo:', err);
            else console.log('✅ Archivo "agenda.txt" creado con éxito.');
            rl.close();
            if (callback) callback(); // Llamamos al siguiente módulo
        });
    }

    console.log('=== AGENDA TELEFÓNICA ===');
    pedirContacto();
}

module.exports = { iniciarDirectorio };
