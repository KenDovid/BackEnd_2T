const var1 = require("./mensaje.js");
console.log(var1);

// Calculadora → luego Agenda
const { iniciarCalculadora } = require('./calculadora');
const { iniciarDirectorio } = require('./directorio');

iniciarCalculadora(() => {
    iniciarDirectorio(() => {
        console.log("✅ Todos los módulos ejecutados correctamente");
    });
});
