function clasificarNota(nota) {
  if (nota >= 70) return "Aprobado";
  else if (nota >= 50) return "Requiere mejora";
  else return "Reprobado";
}

console.log("85 ->", clasificarNota(85));
console.log("60 ->", clasificarNota(60));
console.log("45 ->", clasificarNota(45));
