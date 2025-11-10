const preciosBase = [100, 250, 399, 75];
const preciosConAumento = preciosBase.map(precio => precio * 1.10);
console.log("Originales:", preciosBase);
console.log("Con 10% aumento:", preciosConAumento);
