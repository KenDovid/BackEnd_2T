// Ejercicio 12: Opreaciones al inicio del Array.

let colaClientes = ["Cliete A", "Cliente B", "Cliente C"];
console.log(`Cola inicial: ${colaClientes}`);

// Atender al primer cliente
let atendido = colaClientes.shift();
console.log(`Cliente atendido: ${atendido}`);
console.log(`Coal después de shift: ${colaClientes}`);

// Cliente prioritario al inicio
colaClientes.unshift("Cliente prioritario.");
console.log(`Cola final ${colaClientes}`)