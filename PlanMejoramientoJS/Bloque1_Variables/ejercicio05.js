
const TASA_IMPUESTO = 0.15;
const precioString = "199.99"; // simulación de entrada
const precio = Number(precioString);

if (!isNaN(precio)) {
  const impuesto = precio * TASA_IMPUESTO;
  console.log("Precio base:", precio.toFixed(2));
  console.log("Impuesto (15%):", impuesto.toFixed(2));
} else {
  console.log("Entrada inválida");
}
