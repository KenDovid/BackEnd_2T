class Auto {
  constructor(marca, modelo) {
    this.marca = marca;
    this.modelo = modelo;
  }
  obtenerDescripcion() {
    return `${this.marca} ${this.modelo}`;
  }
}

class VehiculoElectrico extends Auto {
  constructor(marca, modelo, autonomiaBateria) {
    super(marca, modelo);
    this.autonomiaBateria = autonomiaBateria;
  }
  mostrarInfo() {
    return `${super.obtenerDescripcion()}, Autonomía: ${this.autonomiaBateria} km`;
  }
}

const tesla = new VehiculoElectrico("Tesla", "Model 3", 500);
console.log(tesla.mostrarInfo());
