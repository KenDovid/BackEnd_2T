// Ejercicio 15: Arrow Functions

const areaTriangulo = (base, altura) => {
    return(base * altura) / 2
};

// Versión concisa(return implícito)
const areaTrianguloCoroto = (base, altura) =>
    (base * altura) / 2;

console.log(`Area ${areaTriangulo(10,5)}`);
