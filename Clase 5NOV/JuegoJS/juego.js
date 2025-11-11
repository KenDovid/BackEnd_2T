import readline from "readline";
import { personajes, armas, armaduras } from "./base_datos.js";

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

function preguntar(pregunta) {
  return new Promise((resolve) => rl.question(pregunta, (respuesta) => resolve(respuesta)));
}

async function seleccionarOpcion(diccionario, mensaje) {
  const opciones = Object.keys(diccionario);
  let opcionElegida = null;

  while (!opcionElegida) {
    console.log(`\n${mensaje}`);
    opciones.forEach((valor, i) => console.log(`${i + 1}. ${valor}`));

    const opcion = parseInt(await preguntar("Selecciona una opción: "));

    if (opcion >= 1 && opcion <= opciones.length) {
      opcionElegida = opciones[opcion - 1];
      console.log(`\n${opcionElegida}:`);
      for (const [clave, valor] of Object.entries(diccionario[opcionElegida])) {
        console.log(`   ${clave}: ${valor}`);
      }
    } else {
      console.log("Opción no válida, intenta nuevamente.");
    }
  }

  return opcionElegida;
}

export async function crearPersonaje() {
  const name = await preguntar("Ingresa el nombre para tu personaje: ");

  const clase = await seleccionarOpcion(personajes, "Selecciona tu clase de guerrero");
  const arma = await seleccionarOpcion(armas, "Selecciona tu arma");
  const armadura = await seleccionarOpcion(armaduras, "Selecciona tu armadura");

  // Crear stats totales
  const stats = { ...personajes[clase] };
  stats.Vida += armaduras[armadura]["Vida Extra"];
  stats["Armadura Base"] += armaduras[armadura]["Armadura Extra"];
  stats["Daño Base"] += armas[arma]["Daño Extra"];
  stats.Alcance += armas[arma]["Alcance Extra"];

  const personaje = {
    Nombre: name,
    Clase: clase,
    Arma: arma,
    Armadura: armadura,
    Vida: stats.Vida,
    Armadura: stats["Armadura Base"],
    Daño: stats["Daño Base"],
    Alcance: stats.Alcance,
  };

  console.log("\n========================================");
  console.log(`🧝‍♂️ Personaje creado: ${name}`);
  console.log("========================================");
  console.log(`Clase: ${clase}`);
  console.log(`Arma: ${arma}`);
  console.log(`Armadura: ${armadura}`);
  console.log("=== Estadísticas Totales ===");
  for (const [clave, valor] of Object.entries(personaje)) {
    if (!["Nombre", "Clase", "Arma", "Armadura"].includes(clave)) {
      console.log(`   • ${clave}: ${valor}`);
    }
  }

  return personaje;
}

export function cerrarLectura() {
  rl.close();
}
