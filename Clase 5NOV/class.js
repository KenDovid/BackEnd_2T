class Persona {
    constructor(nombre, edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    saludar() {
        return `Hola, soy ${this.nombre}`;
    }

    cumplirAnios() {
        this.edad++;
        return this.edad;
    }
}

const persona1 = new Persona("Jose", 28);

console.log(persona1.saludar());  
console.log(persona1.edad);        
console.log(persona1.cumplirAnios()); 
console.log(persona1.edad);        
