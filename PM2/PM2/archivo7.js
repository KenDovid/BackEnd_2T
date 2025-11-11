// Ejercicio 7: Función para verificar números pares.

function verificarParImpar(numero){
    if(numero %2 === 0){
        console.log(`${numero} es par.`)
    } else {
        console.log(`${numero} es impar.`)
    }
}

// Pruebas
verificarParImpar(15)
verificarParImpar(20)
verificarParImpar(0)
verificarParImpar(-3)