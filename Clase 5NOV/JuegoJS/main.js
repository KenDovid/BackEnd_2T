import { crearPersonaje, cerrarLectura } from "./juego.js";
import { batalla } from "./batalla.js";
import { boss } from "./base_datos.js";

async function iniciarJuego() {
  const jugador = await crearPersonaje();
  await batalla(jugador, boss);
  cerrarLectura();
}

iniciarJuego();
