function iniciarCalculadora(callback) {
    const readline = require('readline');
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    rl.question("Introduce el primer número: ", (num1) => {
        rl.question("Introduce la operación (+, -, *, /): ", (operacion) => {
            rl.question("Introduce el segundo número: ", (num2) => {
                num1 = parseFloat(num1);
                num2 = parseFloat(num2);

                let resultado;
                switch (operacion) {
                    case '+': resultado = num1 + num2; break;
                    case '-': resultado = num1 - num2; break;
                    case '*': resultado = num1 * num2; break;
                    case '/': resultado = num2 !== 0 ? num1 / num2 : "Error: No se puede dividir entre cero."; break;
                    default: resultado = "Operación no válida."; break;
                }

                console.log(`\nResultado: ${resultado}`);
                rl.close();

                if (callback) callback(); // Llamamos al siguiente módulo
            });
        });
    });
}

module.exports = { iniciarCalculadora };
