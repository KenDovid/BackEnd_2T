class Auto {
  constructor(marca, velocidadInicial) {
    this.marca = marca;
    this._velocidad = velocidadInicial;
  }
  set velocidad(valor) {
    if (valor >= 0) this._velocidad = valor;
    else console.log("Error: Velocidad no puede ser negativa");
  }
  get velocidad() {
    return this._velocidad;
  }
}

const carro = new Auto("Ford", 80);
console.log("Velocidad:", carro.velocidad);
carro.velocidad = 120;
console.log("Velocidad nueva:", carro.velocidad);
carro.velocidad = -50; // intento inválido
