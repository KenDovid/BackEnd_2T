function clasificarTemperatura(fahrenheit) {
    if (fahrenheit >= 14 && fahrenheit < 32) {
        return "Temperatura baja";
    } else if (fahrenheit >= 32 && fahrenheit < 68) {
        return "Temperatura adecuada";
    } else if (fahrenheit >= 68 && fahrenheit < 96) {
        return "Temperatura alta";
    } else {
        return "Temperatura desconocida";
    }
}

// Pruebas
console.log(clasificarTemperatura(25)); // "Temperatura baja"
console.log(clasificarTemperatura(50)); // "Temperatura adecuada"
console.log(clasificarTemperatura(85)); // "Temperatura alta"