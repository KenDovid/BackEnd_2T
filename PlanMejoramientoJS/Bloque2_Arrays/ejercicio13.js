let colaClientes = ["Cliente A", "Cliente B", "Cliente C"];
console.log("Cola inicial:", colaClientes);

const atendido = colaClientes.shift();
console.log("Atendido:", atendido);
console.log("Cola después de shift:", colaClientes);

colaClientes.unshift("Cliente Prioritario");
console.log("Cola final:", colaClientes);
