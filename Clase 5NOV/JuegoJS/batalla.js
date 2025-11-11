import readline from "readline";

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

function preguntar(pregunta) {
  return new Promise((resolve) => rl.question(pregunta, (r) => resolve(r)));
}

export async function batalla(jugador, boss) {
  console.log("\n⚔️ ¡Comienza la batalla contra el Boss!");
  console.log(`Te enfrentas a: ${boss.Nombre}\n`);

  let vidaJugador = jugador.Vida;
  let vidaBoss = boss.Vida;
  let defendiendoJugador = false;
  let defendiendoBoss = false;

  while (vidaJugador > 0 && vidaBoss > 0) {
    console.log("\n--- ESTADO ---");
    console.log(`${jugador.Nombre} (Vida: ${vidaJugador}) vs ${boss.Nombre} (Vida: ${vidaBoss})`);

    console.log("\nAcciones disponibles:");
    console.log("1. Atacar");
    console.log("2. Defenderse");
    console.log("3. Esperar");

    const accionJugador = parseInt(await preguntar("Elige tu acción: "));

    if (accionJugador === 1) {
      let dano = jugador.Daño;
      if (defendiendoBoss) dano = Math.floor(dano / 2);
      vidaBoss -= dano;
      console.log(`\n💥 ${jugador.Nombre} ataca y hace ${dano} de daño!`);
      defendiendoJugador = false;
    } else if (accionJugador === 2) {
      defendiendoJugador = true;
      console.log(`\n🛡️ ${jugador.Nombre} se defiende, reducirá el daño recibido!`);
    } else {
      console.log(`\n⏳ ${jugador.Nombre} espera su momento...`);
      defendiendoJugador = false;
    }

    // Turno boss
    const accionBoss = boss.Acciones[Math.floor(Math.random() * boss.Acciones.length)];
    console.log(`\n👉 El Boss decide: ${accionBoss}`);

    if (accionBoss === "Atacar") {
      let dano = boss.Daño;
      if (defendiendoJugador) dano = Math.floor(dano / 2);
      vidaJugador -= dano;
      console.log(`🔥 ${boss.Nombre} ataca e inflige ${dano} de daño!`);
      defendiendoBoss = false;
    } else if (accionBoss === "Defenderse") {
      defendiendoBoss = true;
      console.log(`🛡️ ${boss.Nombre} se defiende!`);
    } else {
      console.log(`😈 ${boss.Nombre} espera...`);
      defendiendoBoss = false;
    }
  }

  console.log("\n=== RESULTADO DE LA BATALLA ===");
  if (vidaJugador <= 0 && vidaBoss <= 0) {
    console.log("😵 Ambos han caído... ¡Empate épico!");
  } else if (vidaBoss <= 0) {
    console.log(`🏆 ¡${jugador.Nombre} ha derrotado al ${boss.Nombre}!`);
  } else {
    console.log(`💀 ${jugador.Nombre} ha sido derrotado por el ${boss.Nombre}...`);
  }

  rl.close();
}
