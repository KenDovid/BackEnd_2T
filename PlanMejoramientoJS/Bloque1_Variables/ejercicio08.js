function verificarParImpar(numero) {
  if (typeof numero !== 'number') {
    console.log("Entrada inválida, se esperaba un número.");
    return;
  }
  console.log(numero, (numero % 2 === 0) ? "es par" : "es impar");
}

// Pruebas
verificarParImpar(15);
verificarParImpar(20);
verificarParImpar(0);
