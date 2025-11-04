let persona = {
  nombre: "Juan",
  edad: 25,
  ciudad: "Madrid"
};

for (let clave in persona) {
  console.log(clave + ":", persona[clave]);
}
