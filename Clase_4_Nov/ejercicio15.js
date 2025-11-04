let estudiantes = [
  { nombre: "Ana", nota: 8 },
  { nombre: "Luis", nota: 5 },
  { nombre: "Marta", nota: 9 }
];

function mostrarAprobados(lista) {
  for (let est of lista) {
    if (est.nota >= 6) {
      console.log(`${est.nombre} ha aprobado con ${est.nota}`);
    } else {
      console.log(`${est.nombre} ha reprobado con ${est.nota}`);
    }
  }
}

mostrarAprobados(estudiantes);
