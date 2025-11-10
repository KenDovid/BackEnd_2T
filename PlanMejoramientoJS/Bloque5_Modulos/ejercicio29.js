class Auto {
  constructor(marca, modelo) {
    this.marca = marca;
    this.modelo = modelo;
  }
  obtenerDescripcion() {
    return `${this.marca} ${this.modelo}`;
  }
}

const vehiculo = new Auto("Nissan", "Sentra");
console.log("Nuevo vehículo:", vehiculo.obtenerDescripcion());
