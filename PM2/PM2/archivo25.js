// Ejercicio 25: Composición de Objetos.

// Composición.js
class Direccion {
    constructor(calle, codigoPostal) {
        this.calle = calle;
        this.codigoPostal = codigoPostal;
    }
}

class Cliente {
    constructor(nombre, direccion) {
        this.nombre = nombre;
        this.direccion = direccion;
    }

    mostrarUbicacion() {
        console.log(`${this.nombre} vive en:
${this.direccion.calle},
CP ${this.direccion.codigoPostal}`);
    }
}

const miDireccion = new Direccion(
    "Avenida Central 456", "10101"
);
const juan = new Cliente("Juan Pérez", miDireccion);
juan.mostrarUbicacion();