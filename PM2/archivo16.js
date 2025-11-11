// Ejercicio 16: Condicional if-else

    function esMayorDeEdad(edad){
        if (edad >= 18){
            return true ;
        } else{
            return false
        }
    }

    // Versión simplificada 
    function esMayorDeEdadSimple(edad){
        return edad >= 18 
    }

console.log(`Edad 20 ${esMayorDeEdad(20)}`);
console.log(`Edad 16 ${esMayorDeEdad(16)}`);