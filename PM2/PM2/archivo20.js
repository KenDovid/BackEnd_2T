// Ejercicio 20: Clase Básica con Constructor

class Auto {
    constructor(marca, modelo) {
        this.marca = marca;
        this.modelo = modelo;
    }

    obtenerDescripcion() {
        return `Marca: ${this.marca}, Modelo: ${this.modelo}`;
    }
}

const miAuto = new Auto("Toyota", "Corolla");
console.log(miAuto.obtenerDescripcion());
// "Marca: Toyota, Modelo: Corolla"

export default Auto;