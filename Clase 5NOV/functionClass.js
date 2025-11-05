function Persona(nombre, apellido, edad) {
    this.nombre = nombre;
    this.apellido = apellido;
    this.edad = edad;
}

Persona.prototype.saludar = function () {
    return `Hola, soy ${this.nombre} ${this.apellido} y tengo ${this.edad} años.`;
}

const persona1 = new Persona("Ana", "Guzmán", 30);
console.log(persona1.saludar());
